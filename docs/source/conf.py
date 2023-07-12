import os, sys
sys.path.insert(0, os.path.abspath('../..'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Template'
copyright = '2023, tomato2718'
author = 'tomato2718'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.mermaid',
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
html_static_path = ['_static']

