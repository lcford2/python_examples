// filename = times.c
/* Purpose: To be used as a shared library */

/*
Return x times y (doubles)
*/
__declspec(dllexport) double times(double x, double y)
{
	double output;
	output = x * y;
	return output;
}

/*
Calculate average of an array (doubles)
*/
__declspec(dllexport) double average(int length, double *values)
{
	double output;
	int i;
	output = 0.0;
	for (i = 0; i < length; i++)
		output += values[i];
	output /= (double)length;
	return output;
}
