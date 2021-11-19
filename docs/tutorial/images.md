# Images

If you like to add an image for your error's page, the suggested way is implementing your custom [simple_tag][simple_tag].

1. Suppose to have your model `MyBackground` to store all your site background's image with a [filer][django-filer] field called `image`.

    ``` python title="example/models.py"
    from django.db import models
    from filer.fields.image import FilerImageField
    
    
    class MyBackground(models.Model):
        name = models.CharField(verbose_name="Background", max_length=50, null=True)
        image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
    ```

2. Upload your images with `name` like the error's code of the page to be able to dynamically load different images with same html file.


3. Create your own template tags to store the image inside the context view where you want to load image

    ``` python title="example/templatetags/errors.py"
    from django import template
    from django.core.cache import cache
    from example.models import MyBackground
    
    register = template.Library()
    
    
    @register.simple_tag(takes_context=True)
    def load_error_img(context):
        cache_key = f"site_error_{context['error_code']}_context"
        try:
            context_cache = cache.get(cache_key)
        except Exception as err:
            context_cache = None
    
        if context_cache is None:
            try:
                custom_context = MyBackground.objects.values('image__file').filter(name=context['error_code']).first()
                context_cache = cache.set(cache_key, custom_context["image__file"], timeout=86400)
                return custom_context["image__file"]
            except Exception as err:
                print(err)
    
        return context_cache or ""
    ```

4. Create your own html template inside the root of your app. Assign the result of your tag `load_error_img` into variable `error_img` and use it with `static` filter.

    ``` html title="example/template/errors.html"
    {% extends 'base.html' %}
    {% load static errors %}
    
    {% block content %}
        
        {% load_error_img as error_img %}
    
        <div style="background-image: url( {% static error_img %} );">
            <strong>Oops! </strong> {{ error_message }}
        </div>
        
    {% endblock content %}
    ```

[simple_tag]: https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/#django.template.Library.simple_tag
[django-filer]: https://github.com/django-cms/django-filer