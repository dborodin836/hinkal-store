# Backend

## Setup

If you don't have [Python](https://www.python.org/downloads/) install it.

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m venv env
$ cd env/Scripts
$ activate
$ cd ../../
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

**NOTE**: If you want run mypy, flake8, black or pytest run:

```sh
(env)$ pip install -r requirements_dev.txt 
```

And finally run the django server:

```sh
$ py manage.py
```


I highly recomend you to create superuser(admin):

```sh
$ py manage.py sadmin
```
This command created superuser:

Login: `admin`

Password: `adminpass`

Use this credentials to login into admin panel (`localhost:8000/admin`).

## Walkthrough

Currently backend has this links:
- `localhost:8000/admin` - standart admin panel
- `localhost:800/api` - api endpoint
- `localhost:800/redoc` - automatic redoc documentations
- `localhost:800/swagger` - automatic swagger documentations
