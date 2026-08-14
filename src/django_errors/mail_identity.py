"""Host mail identity tags for operator Subject/From prefixes.

Mirrors the SH library helper ``SH_Mail_IdentityTag``:

* PROD + core|edge → ``[PROD][core]`` / ``[PROD][edge]`` (hostname omitted)
* Any other scope/role (CLIENT, TEST, allinone, …) → keep hostname
* Optional install label from ``SH_Mail_InstallTag`` / env file

All Django mail (``mail_admins``, ``mail_managers``, and app ``send_mail``
via :func:`prefix_subject`) must use this vocabulary — never invent a
parallel prefix scheme.
"""

from __future__ import annotations

import os
import socket
from pathlib import Path
from typing import Mapping, MutableMapping, Optional

_DEFAULT_ENV_FILE = "/etc/opt/sh/mail-identity.env"
_PROD_COMPACT_ROLES = frozenset({"core", "edge"})


def _read_env_file(path: str | Path) -> dict[str, str]:
    out: dict[str, str] = {}
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return out
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        out[key.strip()] = val.strip()
    return out


def identity_tag(
    *,
    scope: Optional[str] = None,
    role: Optional[str] = None,
    hostname: Optional[str] = None,
    install_tag: Optional[str] = None,
    env_file: str | Path = _DEFAULT_ENV_FILE,
    environ: Optional[Mapping[str, str]] = None,
) -> str:
    """Return the compact identity tag for this host."""
    env = environ if environ is not None else os.environ
    file_vars = _read_env_file(env_file)

    cached = (env.get("SH_MAIL_IDENTITY_TAG") or file_vars.get("SH_MAIL_IDENTITY_TAG") or "").strip()
    if cached and scope is None and role is None and hostname is None and install_tag is None:
        return cached

    scope_v = (scope or env.get("SH_OS_Scope") or file_vars.get("SH_OS_Scope") or "unknown").strip()
    role_v = (role or env.get("SH_Host_Role") or file_vars.get("SH_Host_Role") or "unknown").strip()
    host_v = (
        hostname
        or env.get("SH_OS_HostName")
        or file_vars.get("SH_OS_HostName")
        or socket.gethostname().split(".")[0]
    )
    install_v = (
        install_tag
        if install_tag is not None
        else (env.get("SH_Mail_InstallTag") or file_vars.get("SH_Mail_InstallTag") or "")
    ).strip()

    if scope_v == "PROD" and role_v in _PROD_COMPACT_ROLES:
        tag = f"[{scope_v}][{role_v}]"
    else:
        tag = f"[{scope_v}][{role_v}][{host_v}]"
    if install_v:
        tag = f"{tag}[{install_v}]"
    return tag


def subject_prefix(
    kind: str = "app",
    *,
    environ: Optional[Mapping[str, str]] = None,
    env_file: str | Path = _DEFAULT_ENV_FILE,
) -> str:
    """Return ``[kind]<IdentityTag>`` with trailing space (Django EMAIL_SUBJECT_PREFIX)."""
    env = environ if environ is not None else os.environ
    file_vars = _read_env_file(env_file)
    explicit = (env.get("EMAIL_SUBJECT_PREFIX") or file_vars.get("EMAIL_SUBJECT_PREFIX") or "").rstrip()
    if explicit and kind == "app":
        return f"{explicit} " if not explicit.endswith(" ") else explicit
    return f"[{kind}]{identity_tag(environ=env, env_file=env_file)} "


def prefix_subject(subject: str, *, kind: str = "app") -> str:
    """Prefix a bare subject; leave subjects that already start with ``[`` unchanged."""
    text = subject or ""
    if text.startswith("["):
        return text
    return f"{subject_prefix(kind)}{text}"


def apply_mail_identity_defaults(settings: MutableMapping) -> None:
    """Set ``EMAIL_SUBJECT_PREFIX`` from SH identity (idempotent).

    Call at the end of consumer ``settings.py`` (after storage defaults).
    Does not rewrite ``DEFAULT_FROM_EMAIL`` addresses — only the operator
    Subject vocabulary used by ``mail_admins`` / ``mail_managers``.
    """
    prefix = subject_prefix("app")
    tag = identity_tag()
    if tag and tag != "[unknown][unknown]":
        settings["EMAIL_SUBJECT_PREFIX"] = prefix
        settings["SH_MAIL_IDENTITY_TAG"] = tag
