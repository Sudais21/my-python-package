# -- Project information -----------------------------------------------------
# Project name, copyright, author, and version/release information
project = 'My Python Package'  # Name of your Python package
copyright = '2024, XYZ'        # Copyright information (optional)
author = 'XYZ'                 # Your name or organization
release = '0.1.0'              # Version number of your package

# -- General configuration ---------------------------------------------------
# Extensions that you want to use in your documentation.
# Autodoc will automatically pull docstrings from your Python package.
# Napoleon supports NumPy and Google style docstrings.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

# Add your package directory to the Python path, so autodoc can find it.
# Adjust the path according to where your package is located.
import os
import sys
sys.path.insert(0, os.path.abspath('../my_package'))  # Adjust this path if necessary

# Path to templates, if you have custom templates for your documentation.
templates_path = ['_templates']

# List of patterns to exclude from the build process.
# You can add files or directories here that should not be included in the documentation.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# Theme for the HTML output. You can use 'alabaster' or 'sphinx_rtd_theme' (Read the Docs theme).
# Ensure that you have sphinx_rtd_theme installed (`pip install sphinx_rtd_theme`).
html_theme = 'sphinx_rtd_theme'

# Path to static files (images, CSS, etc.) for customization.
html_static_path = ['_static']

# -- Options for Autodoc ------------------------------------------------------
# Configure autodoc to automatically pull docstrings from your Python files.
autodoc_default_options = {
    'members': True,  # Include all members (methods, attributes) in the docs.
    'undoc-members': True,  # Include undocumented members.
    'show-inheritance': True,  # Show inheritance diagrams in the documentation.
}

# -- Napoleon settings ------------------------------------------------------
# Configure Napoleon extension to support Google and NumPy style docstrings.
napoleon_google_docstring = True  # Enable Google style docstrings.
napoleon_numpy_docstring = True  # Enable NumPy style docstrings.

