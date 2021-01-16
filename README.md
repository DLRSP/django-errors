# django-errors [![PyPi license](https://img.shields.io/pypi/l/django-errors.svg)](https://pypi.python.org/pypi/django_errors)

## Pypi [![PyPi status](https://img.shields.io/pypi/status/django-errors.svg)](https://pypi.python.org/pypi/django_errors) [![PyPi version](https://img.shields.io/pypi/v/django-errors.svg)](https://pypi.python.org/pypi/django_errors) [![PyPi python version](https://img.shields.io/pypi/pyversions/django-errors.svg)](https://pypi.python.org/pypi/django_errors) [![PyPi downloads](https://img.shields.io/pypi/dm/django-errors.svg)](https://pypi.python.org/pypi/django_errors) [![PyPi downloads](https://img.shields.io/pypi/dw/django-errors.svg)](https://pypi.python.org/pypi/django_errors) [![PyPi downloads](https://img.shields.io/pypi/dd/django-errors.svg)](https://pypi.python.org/pypi/django_errors)

```shell
pip install django-errors
```

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-errors.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-errors.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-errors/coverage.svg?branch=master)](https://codecov.io/github/DLRSP/django-errors?branch=master) [![travis-ci.org](https://travis-ci.org/DLRSP/django-errors.svg?branch=master)](https://travis-ci.org/DLRSP/django-errors) [![circleci.com](https://circleci.com/gh/DLRSP/django-errors.svg?style=shield&circle-token=b2c2b63556f8dfc17f9058adfbaae1fd16b3bc01)](https://circleci.com/gh/DLRSP/django-errors)

## Configurations

1. modify `settings.py` by adding the app to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ...
    "django_errors",
    # ...
]
```

2. Finally, modify your project `urls.py` with handlers for all errors:
```python
# ...other imports...
from django_errors import views as errors_views

urlpatterns = [
    # ...other urls...
]

handler400 = errors_views.custom_400
""" Handle 400 error """

handler403 = errors_views.custom_403
""" Handle 403 error """

handler404 = errors_views.custom_404
""" Handle 404 error """

handler500 = errors_views.custom_500
""" Handle 500 error """
```

## Run Example Project

```shell
cd example
python manage.py runserver
```

Now browser the app @ http://127.0.0.1:8000

## About Landing Page Errors
http://www.onextrapixel.com/2011/03/09/the-secret-of-a-successful-error-page-with-35-amazing-404-page-designs/
http://www.onextrapixel.com/2011/10/21/applying-defensive-design-for-the-web/
