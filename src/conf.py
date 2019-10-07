# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinx_bootstrap_theme


# -- Project information -----------------------------------------------------

# project = 'User Interfaces for <br />Programming Languages:<br /><span style="font-weight: normal">A Compendium</span>'
project = 'User Interfaces for Programming Languages'
html_title = project
copyright = '2019. Original content licensed under the Creative Commons Attribution-ShareAlike 4.0 International license.'
author = 'Cyrus Omar'
titlesuffix = "UI for PL"

# The full version, including alpha/beta/rc tags
release = ''
version = release


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_themes']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': 'linear-gradient( #009688, rgba(181, 71, 170, 1) )',
    'display_version': False,
    # 'vcs_pageview_mode': 'edit'
}
html_context = {
    "display_github": True,
    "github_user": "fplab",
    "github_repo": "ui-for-pl",
    "github_version": "master",
    "conf_py_path": "/doc/",
    # "source_suffix": source_suffix
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sourcelink = False

numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section',
}

def setup(app):
    app.add_stylesheet("style-extra.css")
    app.add_javascript("js-extra.js")

latex_elements = {
    'preamble': r'''
\usepackage{cancel}
\providecommand{\require}[1]{}
''',
    'extraclassoptions': 'openany,oneside',
}
