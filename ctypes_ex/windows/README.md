### Compiling the C and Fortran code for windows

I am using Intel Parallel Studio and the C and Fortran Compilers that come with it. 

Open the Intel Developer console packaged with Parallel Studio for your system architecture (64-bit/32-bit). Navigate to the directory where you have stored the C and Fortran source code. Enter the following commands:

* `ifort /dll sum.f90`
* `icl /LD times.c`

This will create two Dynamically Linked Libraries (`sum.dll` and `times.dll`) along with their object files.

Run the `simple_example.py` file to access the `sum` function and `sum_sub` subroutine written in Fortran and the `times` function in written in C. It will print out the solutions to 5.4 * 2.3 and 5.4 + 2.3. 

Run the `timing_ex.py` file to time several different methods of calculating the average of an array of length 1000000. This will print out the average time for the calculation for base python, numpy, an average function in C, and an average function in Fortran. This is designed to demonstrate why you may want to go through the work to write lower-level source code and call it from Python.

The only packages required for this example are:

* `ctypes`
* `numpy`
* `time`