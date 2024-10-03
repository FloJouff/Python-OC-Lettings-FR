Installation
============

1. Prerequisites
----------------

1.1. Python

You must have Python installed on your computer.
For this project, version 3.12 was used.
To download latest version, go to `Python web site <https://www.python.org/> `

1.2. Git

Create an account on gitHub if you don't already have one: 
`GitHub web site <https://github.com/>`
(It is not mandatory to install the application)

1.3. Docker

Finally, create an account on `DockerHub <https://hub.docker.com/>`

2. Clone git repository
------------------------

.. code-block:: console

    cd /path/to/put/project/in
    git clone https://github.com/FloJouff/Python-OC-Lettings-FR.git

3. Create virtual environnement
-------------------------------

.. code-block:: console

    `cd /path/to/Python-OC-Lettings-FR`
    `python -m venv venv`

- Activate environnement:
    macOS / Linux

    .. code-block:: console
        source venv/bin/activate

    Windows

    .. code-block:: console
       venv\scripts\activate

- To deactivate the environment, `deactivate`

4. Install  dependencies
------------------------
.. code-block:: console

    (.env)$ pip install --requirement requirements.txt

5. Initial setup
----------------
For local use, simply create an **.env** file at the root of the project, with the following variables:

   - **SECRET_KEY** : Django secret key
   - **SENTRY_DSN** : Sentry project URL
   - **ALLOWED_HOSTS** : enter allowed host 
   - **DEBUG** : select True or False