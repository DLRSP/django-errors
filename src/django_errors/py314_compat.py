"""Python 3.14 + Django template context copy compatibility.

Django ticket #35844 / PR #18824: on Python 3.14 ``super`` objects became
copyable, so the historical ``BaseContext.__copy__`` implementation that did
``copy(super())`` / ``super().__copy__()`` raises::

    AttributeError: 'super' object has no attribute 'dicts'

This breaks Django admin changelists (inclusion tags), ``{% include … only %}``,
and any ``context.new()`` path. Released Django 5.2.17 still ships the broken
copy; ``stable/5.2.x`` has the upstream rewrite — apply that until a release
includes it.

No-op when the installed Django already uses the fixed implementation or when
running on Python < 3.14.
"""

from __future__ import annotations

import sys
from copy import copy


def _needs_patch() -> bool:
    if sys.version_info < (3, 14):
        return False
    from django.template.context import BaseContext

    sample = BaseContext({"a": 1})
    try:
        copy(sample)
    except AttributeError:
        return True
    return False


def _patched_base_context_copy(self):
    from django.template.context import BaseContext

    duplicate = BaseContext()
    duplicate.__class__ = self.__class__
    duplicate.__dict__ = copy(self.__dict__)
    duplicate.dicts = self.dicts[:]
    return duplicate


def apply() -> bool:
    """Monkey-patch ``BaseContext.__copy__`` when required. Returns True if applied."""
    if not _needs_patch():
        return False
    from django.template.context import BaseContext

    BaseContext.__copy__ = _patched_base_context_copy  # type: ignore[method-assign]
    return True
