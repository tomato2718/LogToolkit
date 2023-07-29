import os, sys
sys.path.insert(0, os.path.abspath('../..'))

from logtoolkit import __about__

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = __about__.__project__
copyright = '2023, tomato2718'
author = __about__.__author__
release = __about__.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton'
]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": False
}
autoclass_content = 'both'
templates_path = ['_templates']
exclude_patterns = []

mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'neutral'});"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = []

