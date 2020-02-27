# 537 Guest Lecture Examples

### Python installation to use these examples
These examples require several python packages that are included in the basic anaconda installation. 
To install anaconda for your platform, you can go the [Anaconda Download](https://www.anaconda.com/distribution/). 
It is best to install Python 3 rather than 2 because 2 will no longer be supported after January 1st, 2020.

### Using `ctypes` to interface with C and Fortran from Python
The code for this example is under the ctypes_ex folder. 
Intel compilers were used to create the linux and windows libraries (x64 architecture). 

In linux, the librarys are called shared objects and have a `.so` extension. The `makefile` shows how the libraries were compiled. 

In windows, the librarys are called dynamically linked libraries (DLL) and have a `.dll` extension. There are instructions in the README.md file that explain how the DLLs were compiled. 


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
The code for this example is under the py_fit_example folder.
If you have installed python through anaconda, the packages required in this example will already be installed. 
This code can be run with an interactive interpreter in Visual Studio Code (VS Code) or exectuted from the command line.
If ran from the command line there will be a lot of output. 

### Optimization - Building algebraic models in Python using Pyomo
The code for this example is under the pyomo_opt folder. 
Pyomo is a Python library built and maintained at Sandia National Labs.
It is designed to allow users to create optimization models with python code and pyomo classes. 
I have used this extensively and it is a very popular, powerful package. It will interface with most commercial and open source solvers. 
The `mixed_product.dat` file contains the data read in by the abstract model created by the `mixed_product_func.py`.
The `mixed_product.py` file creates and solves a concrete model that does not need a data file. 
To use this example you will need to have a mathematical solver installed. These files assume that Gurobi is installed and available for use.
You will also need to install pyomo using the following command:  
    `conda install pyomo`

### Using Google Sheets API to Automatically Create Visualizations
The code for this example is under the gsheets folder.

You can use the environment YAML file to create a conda environment to run this code similar to the one in the PyQt5 section.


Google provides a python api to Google Sheets. This api allows users to read, write, and update spreadsheets from python. 
This can be useful in many scenarios including:

* storing data when you do not want to use a database or do not want to store it locally
* creating visualization dashboards that automatically update
* automatically sharing data with others

This example goes through the process of generating data and pushing it to your google sheet.

### Open Weather API Example
This example pulls 5-day 4-hour forecasted weather data from the Open Weather API and then plots temperature, feels like temperature, and humidity. It serves to demonstrate the ease at which one may pull data from websites if they provide a web API. The `requests` package used here can be used for many other purposes, for example web scraping data that is posted as text files on the internet (e.g. USGS). There are directions for obtaining the API key required for these example in the README.md file in the example folder. 

### Itertools examples
In the itertools_ex folder there is an example of `cycle`. Cycle is a Python function that creates an endless iterator of its input. 
In this example it is used to create a waiting spinner, however it has many more practical uses. 
I plan to continue to update this folder with itertools examples because they unlock some really interesting functionality of Python.
