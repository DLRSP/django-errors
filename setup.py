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
    author='DLRSP',
    author_email='dlrsp.dev@gmail.com',
    packages=['django_errors', ],
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    install_requires=['django_nose',
                      'django<3'],
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
