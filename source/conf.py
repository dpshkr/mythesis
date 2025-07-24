# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Thesis'
copyright = '2025, Pushkar'
author = 'Pushkar'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.bibtex']
bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'super'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
'''
html_theme_options = {
    'logo': 'Figures/iisclogo.png',
    'github_user': 'dpshkr',
    'github_repo': 'mythesis',
    'body_text_align':'justify',
}
'''
