# -*- coding: utf-8 -*-
#

import sys
import os

sys.path.insert(0, os.path.abspath('../src/'))

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Sphinx Autodoc Example'
copyright = u'Ondrej Sika, ondrej@ondrejsika.com'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'SphinxExampledoc'
latex_elements = {
    'papersize': 'a4paper',
    #'preamble': '',
}
latex_documents = [
  ('index', 'SphinxExample.tex', u'Sphinx Autodoc Example Documentation',
   u'Ondrej Sika, ondrej@ondrejsika.com', 'manual'),
]
man_pages = [
    ('index', 'sphinxexample', u'Sphinx Autodoc Example Documentation',
     [u'Ondrej Sika, ondrej@ondrejsika.com'], 1)
]
texinfo_documents = [
  ('index', 'SphinxExample', u'Sphinx Autodoc Example Documentation',
   u'Ondrej Sika, ondrej@ondrejsika.com', 'SphinxExample', 'One line description of project.',
   'Miscellaneous'),
]
autoclass_content = "both"
