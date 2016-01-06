from setuptools import setup

try:
    readme = open('README.md').read()
except:
    readme = u"Wrapper Views for common errors"

from django_errors import __version__ as version

setup(
    name="django_errors",
    version=version,
    url='https://github.com/DLRSP/django-errors',
    license='MIT',
    description="Wrapper Views for common errors",
    author='Davide La Rosa',
    author_email='davide.larosa.coins@gmail.com',
    packages=['django_errors', ],
    long_description=readme,
    include_package_data=True,
    zip_safe=False,
    download_url = 'https://github.com/DLRSP/django-errors/releases/tag/v1.0', # I'll explain this in a second
    install_requires=['django_nose',
		      'django==1.8.7', 
		      ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
