It's an app to wrap Django errors.

---

## Requirements

These packages are required:

* Python (3.6, 3.7, 3.8, 3.9, 3.10)
* Django (2.2, 3.2)

We **highly recommend** and only officially support the latest patch release of each Python and Django series.


## Installation

1. Install using `pip`, including any optional packages you want...

    ``` shell
    pip install django-errors
    ```

    ...or clone the project from github.

    ``` shell
    git clone https://github.com/DLRSP/django-errors/
    ```

2. Add `'django_errors'` to your `INSTALLED_APPS` setting.

    ``` python title="settings.py"
    INSTALLED_APPS = [
        ...
        'django_errors',
    ]
    ```

3. Add the following to your root `urls.py` file.

    ``` python title="urls.py"
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

4. If you would like to handle also the "405 - Method not allowed", add the following middleware to your `MIDDLEWARE` setting.

    ``` python title="settings.py"
    MIDDLEWARE = (
        ...
        "django_errors.middleware.handler.HttpResponseNotAllowedMiddleware",
        ...
    )
    ```

5. If you would like to receive email message for "404 - Not Found" error, add the following middleware at **top** to your `MIDDLEWARE` setting.

    ``` python title="settings.py"
    MIDDLEWARE = (
        "django.middleware.common.BrokenLinkEmailsMiddleware",  # <-- Error Manager 404
        ...
    )
    ```


## Example

Let's take a look at a quick example of using this project to build a simple App with **custom error pages**.

* Browser the demo app on-line on [Heroku][sandbox]
* Check the demo repo on [GitHub][github-demo]

## Quickstart

Can't wait to get started? The [quickstart guide][quickstart] is the fastest way to get up and running and building a **demo App**.

## Customize

Do you want custom solutions? The [customize][customize] section is an overview of which part are easy to design.
If you find how to personalize different scenarios or behaviors, a [pull request][pull-request] is welcome!

## Development

See the [Contribution guidelines][contributing] for information on how to clone  the repository, run the test suite and contribute changes back to django-errors.

## Security

If you believe you’ve found something in this project which has security implications, please **do not raise the issue in a public forum**.

Send a description of the issue via email to [dlrsp.issue@gmail.com][security-mail].  The project maintainers will then work with you to resolve any issues where required, prior to any public disclosure.

## License

MIT License

Copyright (c) 2010-present DLRSP (https://dlrsp.org) and other contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[index]: .
[sandbox]: https://django-errors.herokuapp.com/
[github-demo]: https://github.com/DLRSP/example/tree/django-errors

[quickstart]: tutorial/example.md

[contributing]: community/contributing.md
[pull-request]: community/contributing.png#pull-request

[security-mail]: mailto:dlrsp.issue@gmail.com
