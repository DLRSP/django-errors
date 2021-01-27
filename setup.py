from setuptools import setup
from django_errors import __version__ as version

with open('requirements.txt') as fd:
    requirements = [line.strip() for line in fd if line.strip()]

testing_requirements = [
    'codecov',
    'django_nose',
]

linting_requirements = [
    'flake8',
    'pylint',
    'bandit<1.7',
]

with open('README.md') as fd:
    long_description = fd.read()

if 'a' in version:
    dev_status = '3 - Alpha'
elif 'b' in version:
    dev_status = '4 - Beta'
else:
    dev_status = '5 - Production/Stable'

setup(
    name="django_errors",
    version=version,
    url='https://github.com/DLRSP/django-errors',
    license='MIT',
    description="Wrapper Views for common errors",
    author='DLRSP',
    author_email='dlrsp.dev@gmail.com',
    packages=['django_errors', ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    data_files=[('', ['requirements.txt'])],
    install_requires=requirements,
    tests_require=testing_requirements,
    extras_require={
        'testing': testing_requirements,
        'linting': linting_requirements,
    },
    keywords='python django errors',
    classifiers=[
        f'Development Status :: {dev_status}',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development :: Version Control :: Git :: Libraries :: Python Modules :: Internet :: WWW/HTTP',
    ]
)
