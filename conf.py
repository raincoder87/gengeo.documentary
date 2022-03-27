# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.pardir)))
sys.path.insert(0, os.path.abspath('../..'))
autodoc_mock_imports = ["_tkinter"]


# -- Project information -----------------------------------------------------

project = 'genGEO'
copyright = '2022, Geothermal Energy and Geofluids, ETH Zürich'
author = 'GEG-ETH Zürich'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinx_thebe',
#    "myst_nb",
    "sphinx_copybutton",
    "sphinx_panels",
]

thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "path_to_docs": "docs",
    # "repository_branch": "master",
    # "selector": ".thebe",
    # "selector_input": "",
    # "selector_output": "",
    # "codemirror-theme": "blackboard",  # Doesn't currently work
    # "always_load": True,  # To load thebe on every page
}

myst_enable_extensions = ["colon_fence"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'



html_logo = '../media/logo.jpg'
html_title = 'genGEO Documentation'

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/GEG-ETHZ/genGEO",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "deepnote_url": "https://deepnote.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "logo_only": True,
    "show_toc_level": 2,
    #"launch_buttons": {"thebelab": True},
}



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']



# CopyButton configuration
copybutton_prompt_text = ">>> "
# Switches for testing but shouldn't be activated in the live docs
# copybutton_only_copy_prompt_lines = False
# copybutton_remove_prompts = False
# copybutton_image_path = "test/TEST_COPYBUTTON.png"
# copybutton_selector = "div"

panels_add_bootstrap_css = False

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "SphinxCopybuttondoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "SphinxCopybutton.tex",
        "Sphinx Copybutton Documentation",
        "Chris Holdgraf",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "sphinxcopybutton", "Sphinx Copybutton Documentation", [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "SphinxCopybutton",
        "Sphinx Copybutton Documentation",
        author,
        "SphinxCopybutton",
        "One line description of project.",
        "Miscellaneous",
    ),
]
