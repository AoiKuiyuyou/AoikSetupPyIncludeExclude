[:var_set('', """
# Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:HDLR('heading', 'heading')]\
# AoikSetupPyIncludeExclude
How to include and exclude Python module files and data files in
**setup.py** flexibly.

Tested working with:
- Python 2.7, 3.7
- setuptools 40.9.0
- wheel 0.33.1

## Table of Contents
[:toc(beg='next', indent=-1)]

## Setup
[:tod()]

### Set up source repository
Run:
```
# Download source repository's archive file
wget https://github.com/AoiKuiyuyou/AoikSetupPyIncludeExclude/archive/master.zip -O AoikSetupPyIncludeExclude-master.zip

# Extract the archive file to directory
unzip AoikSetupPyIncludeExclude-master.zip

# Rename the extracted directory
mv -Tv AoikSetupPyIncludeExclude-master AoikSetupPyIncludeExclude
```

### Set up dependency packages
Run:
```
pip install --upgrade setuptools

pip install --upgrade wheel
```

## Usage
[:tod()]

### View source repository contents
The source repository contains these files:
```
|-- .gitignore
|-- LICENSE.txt
|-- README.md
|-- README.src.md
|-- setup.py
|-- src
    |-- AoikSetupPyIncludeExclude.egg-info
    |   |-- PKG-INFO
    |   |-- SOURCES.txt
    |   |-- dependency_links.txt
    |   |-- top_level.txt
    |-- aoiksetuppyincludeexclude
        |-- __init__.py
        |-- excluded_file.txt
        |-- excluded_module.py
        |-- excluded_package
        |   |-- __init__.py
        |   |-- excluded_file.txt
        |   |-- excluded_module.py
        |-- included_file.txt
        |-- included_module.py
        |-- included_package
            |-- __init__.py
            |-- included_file.txt
            |-- included_module.py
```

The goal is to build a source distribution file and a wheel distribution file containing all files in the `src` directory but excluding ones with `excluded` in their name.

This is achieved by overriding several functions used by `setuptools` during building a distribution file so that custom filtering can be applied to include or exclude files. See the [setup.py](/setup.py) file.

### Build source distribution
Build source distribution file:
```
cd AoikSetupPyIncludeExclude

python setup.py clean sdist
```

Files in the source distribution file:
```
|-- PKG-INFO
|-- README.md
|-- setup.cfg
|-- setup.py
|-- src
    |-- AoikSetupPyIncludeExclude.egg-info
    |   |-- PKG-INFO
    |   |-- SOURCES.txt
    |   |-- dependency_links.txt
    |   |-- top_level.txt
    |-- aoiksetuppyincludeexclude
        |-- __init__.py
        |-- included_file.txt
        |-- included_module.py
        |-- included_package
            |-- __init__.py
            |-- included_file.txt
            |-- included_module.py
```

### Build wheel distribution
Build wheel distribution file:
```
cd AoikSetupPyIncludeExclude

python setup.py clean bdist_wheel
```

Files in the wheel distribution file:
```
|-- AoikSetupPyIncludeExclude-0.0.1.dist-info
|   |-- LICENSE.txt
|   |-- METADATA
|   |-- RECORD
|   |-- WHEEL
|   |-- top_level.txt
|-- aoiksetuppyincludeexclude
    |-- __init__.py
    |-- included_file.txt
    |-- included_module.py
    |-- included_package
        |-- __init__.py
        |-- included_file.txt
        |-- included_module.py
```
