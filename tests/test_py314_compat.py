"""Tests for Python 3.14 BaseContext.__copy__ compatibility shim."""

from __future__ import annotations

import copy
import sys

import pytest
from django.template.context import BaseContext, Context, RequestContext
from django.test import RequestFactory

from django_errors import py314_compat


@pytest.mark.skipif(sys.version_info < (3, 14), reason="Py3.14-only regression")
def test_base_context_copy_works_after_apply():
    py314_compat.apply()
    ctx = BaseContext({"x": 1})
    dup = copy.copy(ctx)
    assert dup["x"] == 1
    assert isinstance(dup, BaseContext)
    # second apply is a no-op once copy works
    assert py314_compat.apply() is False


@pytest.mark.skipif(sys.version_info < (3, 14), reason="Py3.14-only regression")
def test_context_new_like_admin_inclusion_tag():
    py314_compat.apply()
    rf = RequestFactory()
    request = rf.get("/MyAdmin/")
    ctx = RequestContext(request, {"cl": object()})
    # admin InclusionAdminNode / library.InclusionNode calls context.new(...)
    child = ctx.new({"opts": object()})
    assert isinstance(child, Context)
