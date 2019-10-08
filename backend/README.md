
Python backend using Django.

This directory contains the Django backend.

For primer on Python and Django using VS Code: https://code.visualstudio.com/docs/python/tutorial-django

Django Documentation: https://docs.djangoproject.com/en/2.2/intro/tutorial01/

# Python Environment

Project includes linting (pylint), code styling (pep8) and testing (pytest) setup via VS Code Settings. Python dependencies are setup within a virtual environment.

## To restore the virtual environment:

 `cd .\kot\backend\`

 `pip install -r requirements.txt`

This will generate `kot\backend\env` containing the projects required python packages.

## To enable the virtual environment (activate.bat provided as convenience):

 `.\env\Scripts\activate`

## To disable the virtual environment (deactivate.bat provided as convenience):

 `.\env\Scripts\deactivate`

## To Update requirements.txt

 Activate environment

 Add new packages using `pip intstall python_package_name`

 `pip freeze > requirements.txt`

# Run Python Development Server

First enable the python envionrment (if not started alrady). See "Python Envionrment" section above.

Then start the server:

 `cd .\kot\backend\src\`

 `python manage.py runserver`

Runs the app in the development mode.<br />
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

# Testing Python

`pytest`

Launches the test runner running all pythong tests.

# Apply DB Migrations

 `cd .\kot\backend\src\`

 `python manage.py makemigrations`
 
 `python manage.py migrate`
