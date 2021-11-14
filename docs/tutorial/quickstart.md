# Quickstart

We're going to create a simple App to allow admin users wrap django errors.

## Example Project setup

Clone the new Django project named `example`

```shell
# Clone the example's project repository
git clone --depth=50 --branch=django-errors https://github.com/DLRSP/example.git example-errors
cd example-errors

# Create a virtual environment to isolate our package dependencies locally
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and django-errors into the virtual environment
pip install -r requirements/py38-django32.txt

# Now sync your database for the first time
python manage.py migrate

# Run the local server
python manage.py runserver
```
