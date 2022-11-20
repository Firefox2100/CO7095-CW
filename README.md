# CO7095-CW

This repository holds the code for CO7095 Course Work, University of Leicester, 2022-2023.

## Disclaimer

This repository is listed under open source license GPL V3.0. The content is provided "as is", without any warranty, including the normally implied warranty for merchantability.

## Usage

### Set up a MySQL database

Please refer to the documents of your preferred database system/engine/etc. on how to set up a MySQL Database. The database has to be compatible with latest standard, and have to be accessible from the environment where backend is going to be. The database this application is developed for is ``MySQL CE 8.0``.

After properly setting up a database, import the ``.sql`` database backup.

### Set up the Flask backend

The backend is written in python with Flask. The Python version this application is developed on is ``Python 3.10``. ``Pypi`` is recommended for dependency set up.

Before running the backend, ensure the following packages are properly installed:

```text
Flask
mysql-connector-python
```

The backend can be run with:

```shell
python <path/to>/flask_app.py
```

Afterwards please check the firewall to make sure the corresponding process can access the port, usually 5000.

### Run the calendar application

First make sure all the source file of the application is located under a findable path for python. The following packages need to be installed:

```text
textual
textual-dev
```

Then, use a **modern, fully interactive terminal** (like powershell on Windows, xfce/gnome terminal on linux, **NOT** an output only terminal), run:

```shell
python <path/to>/calendar_app.py
```

## Testing

The testing sources are developed for ``pytest 7.2.0``, with ``asyncio``, ``raise`` and ``coverage`` plugin set up. **DO NOT** use ``alt-asyncio`` unless time out has been properly set up.

``pytest`` should be able to recognise the test files, and run the functions automatically.
