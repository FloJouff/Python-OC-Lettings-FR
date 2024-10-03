![Python](https://img.shields.io/badge/python-3.12.x-green.svg)
![Django](https://img.shields.io/badge/django-3.0.x-green.svg)

![Pytest](https://img.shields.io/badge/Pytest-8.23.x-blue.svg)
![Coverage](https://img.shields.io/badge/coverage-blue.svg)
![flake8](https://img.shields.io/badge/Flake8 checked.x-brightgreen.svg)
![PEP8](https://img.shields.io/badge/code%20style-pep8-brightgreen.svg)

![Sentry](https://img.shields.io/badge/Sentry-2.14.x-orange.svg)

## Overview

Orange County Lettings web site.
This site puts users in touch with each other to rent or let their property.

## Local development

### Prerequisites

- GitHub account
- DockerHub account
- CircleCI account
- Python interpreter, version 3.6 or higher


#### Clone repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/FloJouff/Python-OC-Lettings-FR.git`

#### Create virtual environnement

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- Activate environnement:
      macOS / Linux
       `source venv/bin/activate`
      Windows
       `venv\scripts\activate`
- To deactivate the environment, `deactivate`

#### Configure a .env file

At the root of your project, create a .env file to store your secret datas

SENTRY_KEY='your link to your sentry page'
SECRET_KEY = 'your django project secret key'
DEBUG=False
ALLOWED_HOSTS=localhost,0.0.0.0,127.0.0.1,'your own adress'.onrender.com

#### Run the site localy

- `cd /path/to/Python-OC-Lettings-FR`
-     macOS / Linux
       `source venv/bin/activate`
      Windows
       `venv\scripts\activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000`in your browser.

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- macOS / Linux
       `source venv/bin/activate`
  Windows
       `venv\scripts\activate`
- `flake8`

#### Unit tests

- `cd /path/to/Python-OC-Lettings-FR`
- macOS / Linux
       `source venv/bin/activate`
  Windows
       `venv\scripts\activate`
Run tests:
- `pytest `
Run tests with the coverage rate:
- `pytest --cov=.`
You can edit a html report: 
- `pytest --cov=. --cov-report html`

#### Administration panel

- Go to `http://localhost:8000/admin`
- Log in as `admin`, password `Abc1234!`.


#### CI/CD Pipeline

- Addition of a CI/CD pipeline with [CircleCI](https://circleci.com)

   1) *Pytest*: run the test suite with pytest
   2) *Linting*: run the linting with flake8
   3) *Dockerisation*: build and push a site image with [Docker](https://www.docker.com) 
   4) *Deploy*: commissioning the site using Render 

#### Deploy with Render

  - [Render](https://render.com/)

#### Setting up a surveillance service

 - Application monitoring and error tracking via [Sentry](https://sentry.io/welcome/)

### Links :
- **[CircleCI Pipeline](https://app.circleci.com/pipelines/circleci/F6BzmJXEFxjQt77WmLxhbF/AajyXrjczUGjJTfMopx3Le)**
- **[Available docker image](https://hub.docker.com/r/flojouff/oc-lettings)**
- **[Application deployed on Render](https://dashboard.render.com/web/srv-crpc6m68ii6s73cfjbj0/)**
- **[Read the Docs]()**