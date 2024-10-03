import os
import sys

from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath('../..'))
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

MOCK_MODULES = ['django', 'django.conf']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

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
    'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = []
autodoc_mock_imports = ["django", "oc_lettings_site"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'haiku'
html_static_path = ['_static']
