# CO7095-CW

This repository holds the code for CO7095 Course Work, University of Leicester, 2022-2023.

## Disclaimer

This repository is listed under open source license GPL V3.0. The content is provided "as is", without any warranty, including the normally implied warranty for merchantability.

## Usage

### Set up Python environment

The first step is to set up a Python environment. The recommended Python version is 3.10. Please also ensure that Python executible and its libraries are in PATH. Most distribution has Python in their package manager, try refering to Python documents on how to set up on your system.

Run the following command to install dependencies:

```shell
sudo pip install -r <path/to/>requirements.txt
```

Then, the python source code should also be in the python findable paths. This project is archived for easily finding the corresponding code, so the importing path in source code is not correctly set up. This can either be achieved by setting your IDE to find then (depending on the IDE of choice), or to simply put all files into the same folder.

### Set up a MySQL database

Please refer to the documents of your preferred database system/engine/etc. on how to set up a MySQL Database. The database has to be compatible with latest standard, and have to be accessible from the environment where backend is going to be. The database this application is developed for is ``MySQL CE 8.0``.

After properly setting up a database, import the ``.sql`` database backup.

Please also ensure that you have an account in MySQL that can access (all priviledges on this schema) the imported database, and that you can use it from your place of running the backend. MySQL account by default disables remote login, so you might need to re-enable it.

### Set up the Flask backend

The backend is written in python with Flask. The Python version this application is developed on is ``Python 3.10``. ``Pypi`` is recommended for dependency set up.

Before running the backend, ensure the following packages are properly installed (already in requirements.txt):

```text
Flask
mysql-connector-python
```

Modify the beginning of the ``flask_app.py`` to use your MySQL instance with your username and password. Then the backend can be run with:

```shell
python <path/to/>flask_app.py
```

Afterwards please check the firewall to make sure the corresponding process can access the port, usually 5000.

### Run the calendar application

First make sure all the source file of the application is located under a findable path for python. The following packages need to be installed (also included in requirements.txt):

```text
textual
textual-dev
```

Modify the URL in ``backend_functions.py`` to point to your running Flask instance. Then, use a **modern, fully interactive terminal** (like powershell on Windows, xfce/gnome terminal on linux, even tools like PuTTY and Termius, **NOT** an output only terminal), run:

```shell
python <path/to>/calendar_app.py
```

## Testing

The testing sources are developed for ``pytest 7.2.0``, with ``asyncio``, ``raise`` and ``coverage`` plugin set up. **DO NOT** use ``alt-asyncio`` unless time out has been properly set up.

``pytest`` should be able to recognise the test files, and run the functions automatically. To run with coverage check, install ``coverage`` with ``pip`` then execute:

```shell
coverage run -m pytest
```

with your choice of parameters. By default, this command runs all tests in the ``tests`` folder. Note that this also requires the source code to be locateable, so another easy solution is to copy them into the ``tests`` folder, or to set up the Python environment correctly. To view coverage report, run:

```shell
coverage report
```

This will show the content of ``.coverage`` report generated in the last ``coverage run``. To run each test file individually and see their test coverage, run:

```shell
coverage run -m pytest <path/to>test_<something>.py
coverage report
```

Note that the built-in tester, like the one in PyCharm, are not based on ``coverage`` and may give wrong coverage information based on your execution method. ``coverage`` focuses only on effective statements, while the built-in ones may consider things irrelevent like blank lines, etc. It's recommended to only use ``coverage`` for this project.
