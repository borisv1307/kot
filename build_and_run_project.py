"""
King of Tokyo game script

This file performs all of the necessary commands in order to build
the project and run the Django server so that the game can be
played locally.
"""

import subprocess
import sys

WINDOWS_COMMAND_PORTIONS = ["cmd.exe", "/c"]

GO_TO_FRONTEND_FOLDER = ["cd", "frontend"]

INSTALL_REACT_REQUIREMENTS = ["npm", "install"]

BUILD_REACT_PROJECT = ["npm", "run", "build"]

GO_TO_BACKEND_FOLDER = ["cd", "backend"]

INSTALL_DJANGO_REQUIREMENTS = ["pip", "install", "-r", "requirements.txt"]

GO_TO_SRC_FROM_BACKEND_FOLDER = ["cd", "src"]

RUN_DJANGO_SERVER = ["python", "manage.py", "runserver"]


def main():
    prepend_command_with = []

    if sys.platform == "win32":
        prepend_command_with = WINDOWS_COMMAND_PORTIONS

    for command in [
        GO_TO_FRONTEND_FOLDER + ["&&"] +
        INSTALL_REACT_REQUIREMENTS + ["&&"] +
        BUILD_REACT_PROJECT,
        GO_TO_BACKEND_FOLDER + ["&&"] +
        INSTALL_DJANGO_REQUIREMENTS + ["&&"] +
        GO_TO_SRC_FROM_BACKEND_FOLDER + ["&&"] +
        RUN_DJANGO_SERVER

    ]:
        subprocess.call(prepend_command_with + command)


if __name__ == "__main__":
    main()
