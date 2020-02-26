### Fitting linear models in Python using `statsmodels` and `sklearn`

This examples goes through some basic `pandas` dataframe manipulation, fitting models with various methods, and plotting the results using `matplotlib`. In the `example.py` file, I attempt to create a model to predict monthly streamflow for a reservoir in Tennessee using precipitation, temperature, previous streamflow, and the Nino3.4 SST Index. The model includes interactions, linear terms, and categorical variables. Some basic diagnostic plots are created and displayed to show the model results. 

This example is designed to ran within Visual Studio Code using the Interactive Python Interpreter. It can be ran from the command line, but there will be a significant amount of terminal output. 

The requisite packages for this example are:
* `pandas`
* `matplotlib`
* `seaborn`
* `numpy`
* `statsmodels`
* `sklearn`

If you installed Python with Anaconda, you should already have these packages installed. 