# %%
import sys
try:
    import pandas as pd
except ModuleNotFoundError as e:
    print("##### conda install pandas #####")
    sys.exit()

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print("##### conda install matplotlib #####")
    sys.exit()

try:
    import numpy as np
except ModuleNotFoundError as e:
    print("##### conda install numpy #####")
    sys.exit()

try:
    import seaborn as sns  # heatmap
except ModuleNotFoundError as e:
    print("##### conda install seaborn #####")
    sys.exit()

# %%
df = pd.read_csv("./electric-flow-data.csv")

# %%
# check the data out
print(df)

# %%
# date is stored as a string, want to convert to datetime type
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# %% Read in ENSO data and append to df
enso = pd.read_csv("./nino3_4.txt", index_col=0,
                   header=None, delim_whitespace=True)
# Unstack and manipulate indexing
enso = enso.transpose().unstack()
new_index = [f"{month}-{int(year)}" for year, month in enso.index]
enso.index = pd.to_datetime(new_index)

# %%
# check the data out
print(enso)

# %%
# Calculate Nino3.4 SST Anomaly index
mean_sst = enso.mean()
enso_anom = enso - mean_sst
nino34_index = enso_anom.rolling(3).mean()


def convert_to_cat(x):
    if x < -0.5:
        return "LaNina"
    elif x > 0.5:
        return "ElNino"
    else:
        return "Normal"


df["Nino34_Index"] = nino34_index.apply(convert_to_cat)

# %%
# check the data out
print(df)

# %%
# I know that streamflow follows a log normal distribution,
# so I am going to add a column with log transformed s-flow
# Going ahead and computing the log for demand as well
df["ln_sFlow"] = np.log(df["sFlow"])
df["ln_dem"] = np.log(df["dem"])

# %%
# I believe sflow and demand exhibit lag1 autocorrelation
# I am going to test this now
print("Streamflow Lag 1 Autocorrelation : {:.3f}".format(
    df["ln_sFlow"].autocorr(1)))
print("Demand Lag 1 Autocorrelation : {:.3f}".format(df["ln_dem"].autocorr(1)))

# %%
# I know I want to include the lag correlation between
# demand and streamflow in my model. I am going to
# lag both variables
df["lag1_sFlow"] = df["sFlow"].shift(1)
df["lag1_ln_sFlow"] = df["ln_sFlow"].shift(1)
df["lag1_dem"] = df["dem"].shift(1)
df["lag1_ln_dem"] = df["ln_dem"].shift(1)
# Since I am considering Nino3.4 Index, I need to consider when it will affect
# the modeled area. I know that there is in general a three month lag correlation
# between the SE US precipitation and Nino3.4 SST
df["Nino34_Index"] = df["Nino34_Index"].shift(3)
df = df.dropna()

# %%
# check out df with new columns
print(df.head())

# %%
# explore correlation matrix to try and determine what
# variables might be important
cor_mat = df.corr()
print(cor_mat)
ax = sns.heatmap(cor_mat, vmin=-1, vmax=1, center=0,
                 cmap=sns.diverging_palette(20, 220, n=200),
                 square=True)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                   horizontalalignment='right')
plt.show()

# %%
# import various linear regression options
# scikit learn
try:
    from sklearn.linear_model import LinearRegression
except ModuleNotFoundError as e:
    print("##### conda install sklearn #####")

# statsmodels
try:
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
except ModuleNotFoundError as e:
    print("##### conda install statsmodels #####")

# %%
# get sflow arrays
sflow_params = df[["precip", "lag1_ln_sFlow"]]
sflow = df["ln_sFlow"]

# %% FITTING MODEL
# Statsmodels
# statsmodels expects a column of ones at the front of the matrix
# if you are going to include an intercept, the 'add_constant'
# method here appends that column for you
sflow_params_c = sm.add_constant(sflow_params)
# Ordinary Least Squares
results = sm.OLS(sflow, sflow_params_c).fit()
statsmodel_preds_1 = results.predict()


print(results.summary())

# %% Fit model similar to R, include temperature
results = smf.ols(
    "ln_sFlow ~ precip + temp + lag1_ln_sFlow + C(Nino34_Index) + precip:lag1_ln_sFlow - 1",
    data=df).fit()
statsmodel_preds_2 = results.predict()
print(results.summary())

# %% FITTING MODEL
# sklearn
lr = LinearRegression()
model = lr.fit(sflow_params, sflow)
rsq = model.score(sflow_params, sflow)
intercept = model.intercept_
sklearn_preds = model.predict(sflow_params)
print("SKLEARN")
print("Rsq          = ", rsq)
print("Intercept    = ", intercept)
print("Beta_1(P)    = ", model.coef_[0])
print("Beta_2(lg1S) = ", model.coef_[1])


# %%
# plot all results
# create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
# plot statsmodels results
ax1.plot(sflow, statsmodel_preds_1, 'ro', label="Preds vs. Actual")
ax1.set_xlabel("Actual", fontsize=16)
ax1.set_ylabel("Predicted", fontsize=16)
ax1.set_title("Statsmodels", fontsize=18)
ax1.plot(ax1.get_xlim(), ax1.get_ylim(), "b--")
# plot sklearn results
ax2.plot(sflow, sklearn_preds, 'ro', label="Preds vs. Actual")
ax2.set_xlabel("Actual", fontsize=16)
ax2.set_title("Sklearn", fontsize=18)
ax2.plot(ax2.get_xlim(), ax2.get_ylim(), "b--")
plt.show()


# %%
try:
    from sklearn import svm
except ModuleNotFoundError as e:
    print("##### conda install sklearn #####")
# Support vector regression
# Another simple method that can be more accurate
# than OLS regression

svr_mod = svm.SVR()
svr_mod.fit(sflow_params, sflow)
rsq = svr_mod.score(sflow_params, sflow)
print("\nSVR Rsquared = {}".format(rsq))  # improved Rsq
svr_preds = svr_mod.predict(sflow_params)

# %%
# plot sklearn model results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

ax1.plot(sflow, sklearn_preds, 'ro', label="Preds vs. Actual")
ax1.set_xlabel("Actual", fontsize=16)
ax1.set_ylabel("Predicted", fontsize=16)
ax1.set_title("OLS", fontsize=18)
ax1.plot(ax1.get_xlim(), ax1.get_ylim(), "b--")

ax2.plot(sflow, svr_preds, 'ro', label="Preds vs. Actual")
ax2.set_xlabel("Actual", fontsize=16)
ax2.set_title("SVR", fontsize=18)
ax2.plot(ax2.get_xlim(), ax2.get_ylim(), "b--")
plt.show()
