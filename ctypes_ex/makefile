
all: times sum

times: times.c
	icc -fpic -shared times.c -otimes.so

sum: sum.f90
	ifort -fpic -shared sum.f90 -osum.so

clean:
	rm *.so