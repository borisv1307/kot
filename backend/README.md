# Python backend using Django

This directory contains the Django backend.

Project includes VS Settings enabling linting (pylint), code styling (pep8) and testing (pytest) setup via VS Code Settings. However, VS Code is not requred. .vscode settings there for those who need it.

Python dependencies are setup within a virtual environment.

## Python Environment

Python dependencies are setup within a virtual environment.

## To restore the virtual environment

`cd \kot`

`python -m venv env`

This will generate `kot\backend\env` containing the projects required python packages. If CLI suggests upgrading PIP or other, use suggested command to do so. Not upgrading can cause isses later.

## To enable the virtual environment (activate.bat provided as convenience)

`.\env\Scripts\activate`

## install dependencies

`pip install -r requirements.txt`

NOTE: PIP or other prompts may suggest upgrading, please do so.

## Run Python Development Server

First enable the python envionrment (if not started alrady). See "Python Envionrment" section above.

Then start the server:

`cd .\kot\backend\src\`

`python manage.py runserver`

Runs the app in the development mode.<br />
Open [http://localhost:8000/](http://localhost:8000/) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

## To disable the virtual environment (deactivate.bat provided as convenience):

`.\env\Scripts\deactivate`

## To Update requirements.txt

Activate environment

Add new packages using `pip intstall python_package_name`

`pip freeze > requirements.txt`

## To Restore Virtual Env using requirements.txt

`cd .\kot\backend\`

`py -m venv env`

`pip install -r requirements.txt`

## Testing Python

`pytest`

Launches the test runner running all pythong tests.

## Apply DB Migrations

`cd .\kot\backend\src\`

`python manage.py makemigrations`

`python manage.py migrate`
