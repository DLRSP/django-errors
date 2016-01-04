# django-errors

![alt text][logo]
[logo]: https://badge.waffle.io/DLRSP/django-errors.png?label=Ready "ToBeWorked"

## Ispired from ..
http://www.onextrapixel.com/2011/03/09/the-secret-of-a-successful-error-page-with-35-amazing-404-page-designs/
http://www.onextrapixel.com/2011/10/21/applying-defensive-design-for-the-web/

## Example Project
http://peterhudec.github.io/authomatic/examples/django-simple.html

First create a new Django project named example ::

	$ django-admin.py startproject example

Inside the newly created example project create a new application named simple ::

	$ cd example
	$ python manage.py syncdb
	$ python manage.py collectstatic
	$ python manage.py runserver 8888
	
Now you browser the app @ http://127.0.0.1:8888/