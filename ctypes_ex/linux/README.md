### `ctypes` examples for C and Fortran for Linux Systems

You can use the `makefile` in this folder to compile the source code to shared objects (linked libraries in linux).

Run the `simple_example.py` file to access the `sum` function and `sum_sub` subroutine written in Fortran and the `times` function in written in C. It will print out the solutions to 5.4 * 2.3 and 5.4 + 2.3. 

Run the `timing_ex.py` file to time several different methods of calculating the average of an array of length 1000000. This will print out the average time for the calculation for base python, numpy, an average function in C, and an average function in Fortran. This is designed to demonstrate why you may want to go through the work to write lower-level source code and call it from Python.

The only packages required for this example are:

* `ctypes`
* `numpy`
* `time`