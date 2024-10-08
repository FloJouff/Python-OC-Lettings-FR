Configuration Guide
===================


1. Environment variables
----------------------------

1.1. List of required variables

For local use, simply create an **.env** file at the root of the project, with the following variables:

   - **SECRET_KEY** : Django secret key
   - **SENTRY_DSN** : Sentry project URL
   - **ALLOWED_HOSTS** : enter allowed host 
   - **DEBUG** : select True or False


2. Database configuration
--------------------------------------

2.1. SQLite

For this project, the database is in the GitHub repository

3. Configuring external services
--------------------------------------

3.1 . Docker Hub

Check out the :doc:`project_on_docker` section for further information

3.2. Render

This project is deployed from Render.
A render account is required.
Render web site <https://render.com/>


3.3. CircleCI

Check out the :doc:`project_cicd` section for further information

3.4 Sentry

Check out the :doc:`surveillance` section for further information