Sample Module Repository
========================

## Python package project structure

If you're not doing a data science project, but just want a quick and dirty file structure for packaging your code as a
Python package, this minimalistic template structure might be useful to you.


## Not for data science projects

For data science projects where you train models, run experiments, 
that sort of thing, I suggest you take a look at my other template:
https://github.com/hviidhenrik/my-sample-data-science-structure

### Usage

1. Create a new repo on GitHub using this as a template.
2. Clone your new repo locally.
3. Change the names of: 
   - the `importname` directory which holds your source code to match your project e.g., `numpy`, 
     if this was the numpy package.*
   - the import statement in `importname/config/__init__.py` should be changed to the same 
     name, e.g., `numpy` for the above example.  
   - `packagename` in setup.py - this is the name of your package and used when installing it in 
     other projects.
4. Using a Python environment of your choice (like conda or virtualenv), install requirements: 
   `pip install -r requirements.txt`
5. Write your code!

*This directory is sometimes called simply `src`, but this could cause problems if you have other custom-built 
packages using this name as this directory will house your source code and thus be used in imports in other projects.

##### Note:

The template comes predefined with some helpful path definitions. See them in: `importname/config/definitions.py`

### Formatting
The files were formatted using isort and black. I recommend running isort to sort imports correctly 
and then format code nicely using black with a line length of 120. Black uses 88 per default, 
but this sometimes causes too many line breaks in my opinion. Just do what makes you happy!

    isort .
    black . --line-length=120

Project Organization
------------

    ├── README.md             <- The top-level README for developers using this project.
    ├── main.py               <- Main script to execute program with sample command line functionality 
    ├── requirements.txt      <- The requirements file for reproducing the analysis environment, e.g.
    │                            generated with `pipreqs .`
    ├── tests                 <- Units tests and test fixtures - I recommend using pytest 
    ├── setup.py              <- makes project pip installable (pip install -e .) so importname can be imported
    ├── importname            <- Source code for use in this project. The name you'll use to import stuff
        ├── __init__.py <- Makes importname a Python module
        ├── config      <- Directory for defitions of paths and other useful stuff
        ├── core.py     <- Core funtionality goes here
        ├── helpers.py  <- Helpers funtions go here



--------
