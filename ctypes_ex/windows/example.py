# filename = example.py
# Purpose: to use shared libraries times.so and sum.so with ctypes

import ctypes as ct
import numpy as np
from IPython import embed as II
from time import process_time_ns as timer

# load librarys
fortran_lib = ct.CDLL("./sum.dll")  # fortran
c_lib = ct.CDLL("./times.dll")  # C
# II()
# * in fortran all arguments are passed by reference, so need to declare as POINTER
sum_function = fortran_lib.SUM  # fortran functon to sum
# specify argument and return types
sum_function.argtypes = (ct.POINTER(ct.c_double), ct.POINTER(ct.c_double))
sum_function.restype = ct.c_double

sum_SR = fortran_lib.SUM_SUB  # fortran subR to sum
# * no res types, return variable is passed as argument
sum_SR.argtypes = (ct.POINTER(ct.c_double), ct.POINTER(
    ct.c_double), ct.POINTER(ct.c_double))

faverage = fortran_lib.AVERAGE  # fortran function to calculate average
faverage.argtypes = (ct.POINTER(ct.c_int), ct.POINTER(ct.c_double))
faverage.restype = ct.c_double

times = c_lib.times  # C function to multiply
# specify argument and return types
times.argtypes = (ct.c_double, ct.c_double)
times.restype = ct.c_double

average = c_lib.average  # C function to find average of an array
# specify argument and return types
average.argtypes = (ct.c_int, ct.POINTER(ct.c_double))
average.restype = ct.c_double

# specify variables using ctypes so they can be passed
x = ct.c_double(5.4)
y = ct.c_double(2.3)
array = [np.random.rand(1)[0] * i for i in range(1000000)]
length = ct.c_int(1000000)
SR_result = ct.c_double(0.0)

# get python values to compare with
actual_times = 5.4 * 2.3
actual_sum = 5.4 + 2.3
actual_average = sum(array) / length.value

times_result = times(x, y)
sumf_result = sum_function(x, y)
sum_SR(x, y, SR_result)
# * array still python object, need to convert it to a ctype array
array_type = ct.c_double * length.value
average_result = average(length, array_type(*array))

print(
    f"\nC Times    = {times_result:-10.2f}, Python Times   = {actual_times:-10.2f}"
)
print(
    f"F Sum Func = {sumf_result:-10.2f}, Python Sum     = {actual_sum:-10.2f}"
)
print(
    f"F Sum SubR = {SR_result.value:-10.2f}, Python Sum     = {actual_sum:-10.2f}"
)
print(
    f"C Average  = {average_result:-10.2f}, Python Average = {actual_average:-10.2f}"
)


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
