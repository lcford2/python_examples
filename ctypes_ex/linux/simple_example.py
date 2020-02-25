import ctypes as ct

# load librarys
fortran_lib = ct.CDLL("./sum.so")  # fortran
c_lib = ct.CDLL("./times.so")  # C

# * in fortran all arguments are passed by reference, so need to declare as POINTER
# * Also, in windows, fortran function names are converted to uppercase
sum_function = fortran_lib.sum_  # fortran functon to sum
# specify argument and return types
sum_function.argtypes = (ct.POINTER(ct.c_double), ct.POINTER(ct.c_double))
sum_function.restype = ct.c_double

sum_SR = fortran_lib.sum_sub_  # fortran subR to sum
# * no res types, return variable is passed as argument
sum_SR.argtypes = (ct.POINTER(ct.c_double), ct.POINTER(
    ct.c_double), ct.POINTER(ct.c_double))

times = c_lib.times  # C function to multiply
# specify argument and return types
times.argtypes = (ct.c_double, ct.c_double)
times.restype = ct.c_double

x = ct.c_double(5.4)
y = ct.c_double(2.3)
SR_result = ct.c_double(0.0)

times_result = times(x, y)
sumf_result = sum_function(x, y)
sum_SR(x, y, SR_result)

actual_times = 5.4 * 2.3
actual_sum = 5.4 + 2.3

print(
    f"\nC Times    = {times_result:-10.2f}, Python Times   = {actual_times:-10.2f}"
)
print(
    f"F Sum Func = {sumf_result:-10.2f}, Python Sum     = {actual_sum:-10.2f}"
)
print(
    f"F Sum SubR = {SR_result.value:-10.2f}, Python Sum     = {actual_sum:-10.2f}"
)
