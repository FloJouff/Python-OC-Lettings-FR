Docker
======

1. Dockerfile presentation
---------------------------

The Dockerfile will be loaded automatically from the GitHub repo

2. Docker image Construction
-----------------------------

You must download and install docker:

`Docker <https://docs.docker.com/get-started/get-docker/>`

Then you can build your docker image:

(Replace image-name with the desired name)

.. code-block:: console

    (.venv)$ docker build -t <image-name>

3. Running the docker container
-------------------------------

You can run locally your docker image to test it: 

.. code-block:: console

    (.venv)$ docker run -d -p 8000:8000 <image-name>

You can access the app in any web browser at http://127.0.0.1:8000/

4. Push your Docker image on DockerHub
--------------------------------------
Once you have created your Docker image, you can push it onto DockerHub to make it accessible to CircleCI.

.. code-block:: console

    (.venv)$ docker tag ocr-docker-build:latest YOUR_USERNAME/<image-name>

This command line will create a link between our docker latest image created earlier and the image we want to send to the Docker Hub 

.. code-block:: console
    
    (.venv)$ docker push YOUR_USERNAME/<image-name>