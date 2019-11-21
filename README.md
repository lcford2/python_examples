# 537 Guest Lecture Examples

### Python installation to use these examples
These examples require several python packages that are included in the basic anaconda installation. 
To install anaconda for your platform, you can go the [Anaconda Download](https://www.anaconda.com/distribution/). 
It is best to install Python 3 rather than 2 because 2 will no longer be supported after January 1st, 2020.

### Using `ctypes` to interface with C and Fortran from Python
The code for this example is under the ctypes_ex folder. 
The shared objects (.so files) were compiled with intel compiler in a linux environment.
If you plan to use this with other compilers update the makefile. 
If you are planning to use this in a windows environment you will need to follow the same basic structure of the makefile, but using specific compiler directives to get a .dll instead of an .so.

The python packages required for this example are:  
- ctypes 
- numpy
- time

### Using `PyQt5` to make a simple GUI in Python
The code for this example is under the econ_gui folder. 
This folder contains an `environment.yml` file that can be used to create a conda environment suitable for this example.
To create the environment, type the following into your command line from the econ_gui directory:  
    `conda env create -f environment.yml` 

To run the interface, execure the following commands from the command line in the econ_gui directory:  
    `conda activate qt-env`  
    `python econ_gui.py`  

### Fitting linear models to data and plotting results with Python
The code for this example is under the PyFitExamples folder.
If you have installed python through anaconda, the packages required in this example will already be installed. 
This code can be run with an interactive interpreter in Visual Studio Code (VS Code) or exectuted from the command line.

### Optimization - Building algebraic models in Python using Pyomo
The code for this example is under the pyomo_opt folder. 
Pyomo is a Python library built and maintained at Sandia National Labs.
It is designed to allow users to create optimization models with python code and pyomo classes. 
I have used this extensively and it is a very popular, powerful package. It will interface with most commercial and open source solvers. 
The `mixed_product.dat` file contains the data read in by the abstract model created by the `mixed_product_func.py`.
The `mixed_product.py` file creates and solves a concrete model that does not need a data file. 
To use this example you will need to have a mathematical solver installed. These files assume that Gurobi is installed and availble for use.
You will also need to install pyomo using the following command:  
    `pip install pyomo`
