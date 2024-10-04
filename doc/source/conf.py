import os
import sys

from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath('../..'))


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = ['django', 'django.conf', 'django.db', 'django.db.models',
                'django.contrib', 'django.contrib.auth',
                'django.contrib.auth.models', 'django.shortcuts', 'django.http', 'sentry_sdk']


for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = MagicMock()

os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OC-Lettings'
copyright = '2024, Florian Jouffroy'
author = 'Florian Jouffroy'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    ]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/stable/',
               'https://docs.djangoproject.com/en/stable/_objects/'),
}

templates_path = ['_templates']
exclude_patterns = []
autodoc_mock_imports = ["django", "oc_lettings_site", "lettings", "profiles",
                        "django.shortcuts", "django.core.exceptions"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'haiku'
html_static_path = ['_static']
