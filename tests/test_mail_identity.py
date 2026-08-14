"""Mail identity tag parity with SH_Mail_IdentityTag."""

import os
from pathlib import Path

from django_errors.mail_identity import (
    apply_mail_identity_defaults,
    identity_tag,
    prefix_subject,
    subject_prefix,
)


def test_prod_core_omits_hostname():
    tag = identity_tag(
        scope="PROD",
        role="core",
        hostname="centos-10-core",
        install_tag="",
        environ={},
        env_file=Path(os.devnull),
    )
    assert tag == "[PROD][core]"


def test_prod_edge_omits_hostname():
    tag = identity_tag(
        scope="PROD",
        role="edge",
        hostname="centos-10-edge",
        install_tag="",
        environ={},
        env_file=Path(os.devnull),
    )
    assert tag == "[PROD][edge]"


def test_client_keeps_hostname_and_install():
    tag = identity_tag(
        scope="CLIENT",
        role="satellite",
        hostname="client-pihole-1",
        install_tag="pihole-a",
        environ={},
        env_file=Path(os.devnull),
    )
    assert tag == "[CLIENT][satellite][client-pihole-1][pihole-a]"


def test_test_scope_keeps_hostname():
    tag = identity_tag(
        scope="TEST",
        role="edge",
        hostname="lab-edge",
        install_tag="",
        environ={},
        env_file=Path(os.devnull),
    )
    assert tag == "[TEST][edge][lab-edge]"


def test_subject_prefix_and_prefix_subject(monkeypatch):
    monkeypatch.delenv("SH_MAIL_IDENTITY_TAG", raising=False)
    monkeypatch.delenv("EMAIL_SUBJECT_PREFIX", raising=False)
    monkeypatch.setenv("SH_OS_Scope", "PROD")
    monkeypatch.setenv("SH_Host_Role", "core")
    monkeypatch.setenv("SH_OS_HostName", "centos-10-core")
    monkeypatch.setenv("SH_Mail_InstallTag", "")
    env = {
        "SH_OS_Scope": "PROD",
        "SH_Host_Role": "core",
        "SH_OS_HostName": "centos-10-core",
    }
    pref = subject_prefix("app", environ=env, env_file=Path(os.devnull))
    assert pref == "[app][PROD][core] "
    assert prefix_subject("TrashScan") == "[app][PROD][core] TrashScan"
    assert prefix_subject("[already] tagged") == "[already] tagged"


def test_apply_mail_identity_defaults(tmp_path, monkeypatch):
    env_path = tmp_path / "mail-identity.env"
    env_path.write_text(
        "SH_MAIL_IDENTITY_TAG=[PROD][edge]\n"
        "EMAIL_SUBJECT_PREFIX=[app][PROD][edge] \n",
        encoding="utf-8",
    )
    monkeypatch.delenv("SH_MAIL_IDENTITY_TAG", raising=False)
    monkeypatch.delenv("EMAIL_SUBJECT_PREFIX", raising=False)
    monkeypatch.delenv("SH_OS_Scope", raising=False)
    monkeypatch.delenv("SH_Host_Role", raising=False)
    settings = {"EMAIL_SUBJECT_PREFIX": "[Django] "}
    from django_errors import mail_identity as mi

    monkeypatch.setattr(mi, "_DEFAULT_ENV_FILE", str(env_path))
    apply_mail_identity_defaults(settings)
    assert settings["EMAIL_SUBJECT_PREFIX"] == "[app][PROD][edge] "
    assert settings["SH_MAIL_IDENTITY_TAG"] == "[PROD][edge]"
