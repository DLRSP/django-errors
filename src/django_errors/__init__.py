"""
See PEP 386 (http://www.python.org/dev/peps/pep-0386/)
Release logic:
1. Remove "dev" from current.
2. git commit
3. git tag <version>
4. push to pypi + push to github
5. bump the version, append '.dev0'
6. git commit
7. push to github (to avoid confusion)
"""
import django

__version__ = "1.5.2"
__license__ = "MIT"
__title__ = "django_errors"

__author__ = "DLRSP"
__copyright__ = "Copyright 2010-present DLRSP"

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

# Default datetime input and output formats
ISO_8601 = "iso-8601"

if django.VERSION < (3, 2):
    default_app_config = "django_errors.apps.DjangoErrorsConfig"
