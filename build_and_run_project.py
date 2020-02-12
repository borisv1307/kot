"""
King of Tokyo game script

This file performs all of the necessary commands in order to build
the project and run the Django server so that the game can be
played locally.
"""

import subprocess
import sys


> `cd \kot\backend\` </br>
> `python -m venv env` </br>
> `.\env\Scripts\activate` </br>
> `pip install -r requirements.txt`</br>
> `python -m pip install --upgrade pip`</br>
> `pip install -r requirements.txt`</br>
> `python manage.py runserver` </br>

WINDOWS_COMMAND_PORTIONS = ["cmd.exe", "/c"]

GO_TO_FRONTEND_FOLDER = ["cd", "frontend"]

INSTALL_REACT_REQUIREMENTS = ["npm", "install"]

BUILD_REACT_PROJECT = ["npm", "run", "build"]

GO_BACK_A_FOLDER = ["cd.."]

GO_TO_BACKEND_FOLDER = ["cd", "backend"]

INSTALL_DJANGO_REQUIREMENTS = ["pip", "install", "-r", "requirements.txt"]

UPGRADE_PIP = ["python", "-m", "pip", "install", "--upgrade", "pip"]

GO_TO_SRC_FROM_BACKEND_FOLDER = ["cd", "src"]

RUN_DJANGO_MIGRATE = ["python", "manage.py", "migrate"]

RUN_DJANGO_SERVER = ["python", "manage.py", "runserver"]


def main():
    prepend_command_with = []

    if sys.platform == "win32":
        prepend_command_with = WINDOWS_COMMAND_PORTIONS

    for command in [
        GO_TO_FRONTEND_FOLDER + ["&&"] +
        INSTALL_REACT_REQUIREMENTS + ["&&"] +
        BUILD_REACT_PROJECT,
        GO_BACK_A_FOLDER,
        GO_TO_BACKEND_FOLDER + ["&&"] +
        INSTALL_DJANGO_REQUIREMENTS + ["&&"] +
        UPGRADE_PIP + ["&&"] +
        GO_TO_SRC_FROM_BACKEND_FOLDER + ["&&"] +
        RUN_DJANGO_MIGRATE +
        RUN_DJANGO_SERVER

    ]:
        subprocess.call(prepend_command_with + command)


if __name__ == "__main__":
    main()
