# Templates

You can overwrite each page's template by create your own html file inside `example/templates/errors/404.html`

You can also overwrite one or all page's template by settings your own html file inside `settings`

``` python title="settings.py"
# Custom Templates for all errors page inside the root's templates of my app
TEMPLATE_ERROR_ALL = "general_errors_page.html"

# Custom Templates for only 404 error's inside the root's templates of my app
TEMPLATE_ERROR_404 = "other_error_page.html"

# Custom Templates for only 405 error's inside the custom_app's templates
TEMPLATE_ERROR_405 = "custom_app/another_error_page.html"
```

All available `settings` variables are:
``` python title="settings.py"
TEMPLATE_ERROR_ALL = "errors/errors.html"
TEMPLATE_ERROR_400 = "errors/400.html"
TEMPLATE_ERROR_403 = "errors/403.html"
TEMPLATE_ERROR_404 = "errors/404.html"
TEMPLATE_ERROR_405 = "errors/405.html"
TEMPLATE_ERROR_500 = "errors/500.html"
```

The order to find template is:

1. Custom template for specific error page (example: `settings.TEMPLATE_ERROR_404`)
2. Custom template for all errors page (example: `settings.TEMPLATE_ERROR_ALL`)
3. Custom template for specific error page by to overwrite default (example: `example/templates/errors/404.html`)
4. Default template for specific error page
