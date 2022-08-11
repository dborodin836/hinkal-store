# Backend

## Setup

If you don't have [Python](https://www.python.org/downloads/) install it.
If you don't have [PostgreSQL](https://www.postgresql.org/download/) install it.

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

**Before applying migration you must create `.env` file in `hinkali-store` directory. And expose an environment variable.**

Available vars are:

- "DEV" - local development
- "PROD" - production
- "DOCKER" - user to containerize app (no need to set it up manually)
- "TEST" - used to test app with GH actions

**NOTE: Not all corresponding file are available in gh repository.**

**You can find an example in `hinkali-store/backend/docs/.env_template.md`**

Apply the migration:

```sh
$ py manage.py makemigrations
$ py manage.py migrate
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

## Running Tests

To run tests, expose "ENV=dev" variable and run the following command

```bash
  $ py backend/manage.py test
```
