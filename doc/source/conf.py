import os
import sys

import django

sys.path.insert(0, os.path.abspath('../..'))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

django.setup()
# autodoc_mock_imports = ["lettings", "profiles", "oc_lettings_site"]

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
    ]

autodoc_modules = {
    "lettings": "lettings",
    "profiles": "profiles",
    "oc_lettings_site": "oc_lettings_site",
}
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
