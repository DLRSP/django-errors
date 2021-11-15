# django-errors [![PyPi license](https://img.shields.io/pypi/l/django-errors.svg)](https://pypi.python.org/pypi/django_errors)

[![PyPi status](https://img.shields.io/pypi/status/django-errors.svg)](https://pypi.python.org/pypi/django_errors)
[![PyPi version](https://img.shields.io/pypi/v/django-errors.svg)](https://pypi.python.org/pypi/django_errors)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-errors.svg)](https://pypi.python.org/pypi/django_errors)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-errors.svg)](https://pypi.python.org/pypi/django_errors)
[![PyPi downloads](https://img.shields.io/pypi/dw/django-errors.svg)](https://pypi.python.org/pypi/django_errors)
[![PyPi downloads](https://img.shields.io/pypi/dd/django-errors.svg)](https://pypi.python.org/pypi/django_errors)

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-errors.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-errors.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-errors/coverage.svg?branch=master)](https://codecov.io/github/DLRSP/django-errors?branch=master) [![travis-ci.org](https://travis-ci.org/DLRSP/django-errors.svg?branch=master)](https://travis-ci.org/DLRSP/django-errors) [![gitthub.com](https://github.com/DLRSP/django-errors/actions/workflows/ci.yml/badge.svg)](https://github.com/DLRSP/django-errors/actions/workflows/ci.yml)

## Check Demo Project
* Browser the demo app on-line on [Heroku](https://django-errors.herokuapp.com/)
* Check the demo repo on [GitHub](https://github.com/DLRSP/example/tree/django-errors)

## Requirements
-   Python 3.6 to 3.10 supported.
-   Django 2.2 to 4.0 supported.

## Setup
1. Install from **pip**:
```shell
pip install django-errors
```

2. modify `settings.py` by adding the app to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ...
    "django_errors",
    # ...
]
```

3. Finally, modify your project `urls.py` with handlers for all errors:
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
git clone --depth=50 --branch=django-errors https://github.com/DLRSP/example.git DLRSP/example
cd DLRSP/example
python manage.py runserver
```

Now browser the app @ http://127.0.0.1:8000

