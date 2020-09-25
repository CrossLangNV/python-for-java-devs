# Automatic documenetation with Sphinx

## Initialisation

Initiate Sphinx basic files:

    $ sphinx-quickstart
    

## Configuration

Adjust `conf.py`: 
* uncomment 
* change path.


    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
    
* add extensions:


    extensions = [
    'sphinx.ext.autodoc'
    ]
    
* A more modern look: (after installing it: pip install sphinx_rtd_theme)


    html_theme = 'sphinx_rtd_theme'    
   
   
* Also include constructors (__init__) docstrings
https://stackoverflow.com/a/9772922/6921921


    autoclass_content = 'both'
    
# Including modules
    
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
sphinx-apidoc -o source/ ..
`

`
make html
`

### Possibly useful commands:

`
make clean
`

# Github website

When uploading to github, to use as webpage, move the **./html** folder to **/docs**.
