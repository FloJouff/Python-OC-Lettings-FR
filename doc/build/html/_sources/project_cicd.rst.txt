Deployment
==========


1. Configuration de CircleCI
----------------------------

2.1. .circleci/config.yml configuration file.

This file was downloaded with the github repository.

2.2. CircleCI environnment variables:

You must specify the variables linked to Docker Hub:

    - **DOCKER_LOGIN**: Your connexion email to your dockerHub account
    - **DOCKER_PASSWORD**: Docker Hub password
    - **DOCKER_USERNAME**: Docker Hub username

The variables linked to Render use must be set in the CircleCI environment variables.

   - **HOOK_RENDER**: go to settings - Deploy hook

2. Deployment on Render
-------------------------

2.1. Configuring the service on Render

This project is deployed from Render.
A render account is required.
`Render web site <https://render.com/>` 

In the **environment** section of the project, enter the environment variables present in the **.env** file:
    - **SECRET_KEY** : Django secret key
    - **SENTRY_DSN** : Sentry project URL
    - **ALLOWED_HOSTS** : enter allowed host 
    - **DEBUG** : select True or False

2.2. Automatic deployment via CircleCI

Each time you commit to the main/master branch of the project on GitHub, the deployment will take place automatically from Render after the docker image has been built and the various pre-deployment tests have been run on CircleCI.

3. Post-deployment verification
--------------------------------

To check that deployment is proceeding correctly, you can make a small change to the project index page and ensure that this change is visible at the address specified by docker (for example: `<https://fj-oc-lettings.onrender.com>` ).