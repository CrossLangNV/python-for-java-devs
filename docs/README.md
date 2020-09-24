`
sphinx-quickstart
`

#

Adjust conf.py (uncomment + change path)

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
    
and add to extensions:

    extensions = [
    'sphinx.ext.autodoc'
    ]
    
A more modern look: (after installing it: pip install sphinx_rtd_theme)

    html_theme = 'sphinx_rtd_theme'    
   
   
Also include constructor (__init__) 
https://stackoverflow.com/a/9772922/6921921

    autoclass_content = 'both'
    
#
    
Add modules to index.rst


    .. toctree::
       :maxdepth: 2
       :caption: Contents:
       
       modules
    
It makes a modules.rst with all the module paths.

## ! WARNING

if there are new modules added, you might have to manually adjust modules.rst!
#  
`
sphinx-apidoc -o . ..
`

`
make html
`

### Possibly useful commands:

`
make clean
`