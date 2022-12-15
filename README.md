<p align="center">
  <img src="https://i.postimg.cc/wMHtRZft/image-removebg-preview-1.png" alt="Logo" width="40%"/>
</p>
  <h3 align="center">Food Marketplace 'HINKAL'</h3>
  <p align="center">
    Fullstack website created for interview.
    <br/>
    <br/>
  </p>
</p>

[![Code style: black][black-badge]][black-link]
<img src="https://img.shields.io/github/license/dborodin836/marketplace-hinkal" alt="License">
<img src="https://img.shields.io/github/checks-status/dborodin836/marketplace-hinkal/develop" alt="Checks">
<img src="https://img.shields.io/github/last-commit/dborodin836/marketplace-hinkal" alt="Last commit">
<img src="http://img.shields.io/github/actions/workflow/status/dborodin836/marketplace-hinkal/ci.yml?branch=develop" alt="Build status">
<img src="https://img.shields.io/github/commit-activity/m/dborodin836/marketplace-hinkal" alt="Commit activity">
<img src="https://www.codefactor.io/repository/github/dborodin836/marketplace-hinkal/badge" alt="Codefactor">
[![DeepSource][deepsource-badge]][deepsource-link]


## Coverage
| **Backend**                                       | **Frontend**                                       | **Total**                                 |
|:-------------------------------------------------:|:--------------------------------------------------:|:-----------------------------------------:|
| [![codecov][codecov-backend-badge]][codecov-link] | [![codecov][codecov-frontend-badge]][codecov-link] | [![codecov][codecov-badge]][codecov-link] |


## Table Of Contents

- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Usage](#usage)

## About The Project

[![image.png](https://i.postimg.cc/PqzS6R0H/image.png)](https://postimg.cc/06jGjc8X)

Main features:

- Ordering dishes with different modifiers (additional sauce etc.)
- Custom users and vendors
- Administration

I hope that site will be awesome soon :smile:

## Built With

Frontend:

- [Angular](https://angular.io)

Backend:

- [Django](https://www.djangoproject.com)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [PostgreSQL](https://www.postgresql.org)
- [Pgbouncer](https://www.pgbouncer.org)

## Getting Started

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/dborodin836/marketplace-hinkal.git
$ cd marketplace-hinkal
```

The easiest way to start project is requires Docker,
If you don't have Docker [install it](https://docs.docker.com/get-docker/).
And run simple command.

**This could take a while...**

```sh
$  docker-compose -f .\docker-compose-local.yml up
```

Alternatively, you can do setup manually following guides in specific folders.

## Usage

- Screenshots and addition description, usage \*

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/psf/black
[deepsource-badge]: https://deepsource.io/gh/dborodin836/marketplace-hinkal.svg/?label=active+issues&token=IHInroIWzClOi9afsigBuueu
[deepsource-link]: https://deepsource.io/gh/dborodin836/marketplace-hinkal/?ref=repository-badge
[codecov-backend-badge]: https://codecov.io/gh/dborodin836/marketplace-hinkal/branch/develop/graph/badge.svg?token=VLZPPIYUOG&flag=backend
[codecov-frontend-badge]: https://codecov.io/gh/dborodin836/marketplace-hinkal/branch/develop/graph/badge.svg?token=VLZPPIYUOG&flag=frontend
[codecov-badge]: https://codecov.io/gh/dborodin836/marketplace-hinkal/branch/develop/graph/badge.svg?token=VLZPPIYUOG
[codecov-link]: https://codecov.io/gh/dborodin836/marketplace-hinkal
