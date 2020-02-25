### Compiling the C and Fortran code for windows

I am using Intel Parallel Studio and the C and Fortran Compilers that come with it. 

Open the Intel Developer console packaged with Parallel Studio for your system architecture (64-bit/32-bit). Navigate to the directory where you have stored the C and Fortran source code. Enter the following commands:

* `ifort /dll sum.f90`
* `icl /LD times.c`

This will create two Dynamically Linked Libraries (`sum.dll` and `times.dll`) along with their object files.