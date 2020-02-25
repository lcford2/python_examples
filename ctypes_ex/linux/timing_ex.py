# filename = example.py
# Purpose: to use shared libraries times.so and sum.so with ctypes

import ctypes as ct
import numpy as np
from time import process_time_ns as timer

# load librarys
fortran_lib = ct.CDLL("./sum.so")  # fortran
c_lib = ct.CDLL("./times.so")  # C

faverage = fortran_lib.average_  # fortran function to calculate average
faverage.argtypes = (ct.POINTER(ct.c_int), ct.POINTER(ct.c_double))
faverage.restype = ct.c_double

average = c_lib.average  # C function to find average of an array
# specify argument and return types
average.argtypes = (ct.c_int, ct.POINTER(ct.c_double))
average.restype = ct.c_double

# specify variables using ctypes so they can be passed
array = [np.random.rand(1)[0] * i for i in range(1000000)]
length = ct.c_int(1000000)

# * array still python object, need to convert it to a ctype array
array_type = ct.c_double * length.value

# time average calculation, show why this may be useful
time1 = timer()
for i in range(100):
    actual_average = sum(array) / length.value
time2 = timer()
py_time = time2 - time1

nparray = np.array(array)
time1 = timer()
for i in range(100):
    average_result = nparray.mean()
time2 = timer()
np_time = time2 - time1

pass_array = array_type(*array)
time1 = timer()
for i in range(100):
    average_result = average(length, pass_array)
time2 = timer()
c_time = time2 - time1

time1 = timer()
for i in range(100):
    average_result = faverage(length, pass_array)
time2 = timer()
f_time = time2 - time1


print(
    f"\nAverage NumPy Time {np_time/(10**9*100):.5f} secs, Average Python Time {py_time/(10**9*100):.5f} secs"
)
print("Using Numpy is {:.2f} times faster\n".format(py_time / np_time))

print(
    f"\nAverage C Time {c_time/(10**9*100):.5f} secs, Average Python Time {py_time/(10**9*100):.5f} secs"
)
print("Calling C is {:.2f} times faster\n".format(py_time / c_time))

print(
    f"\nAverage Fortran Time {f_time/(10**9*100):.5f} secs, Average Python Time {py_time/(10**9*100):.5f} secs"
)
print("Calling Fortran is {:.2f} times faster\n".format(py_time / f_time))
