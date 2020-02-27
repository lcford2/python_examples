import requests
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import datetime
import sys
from IPython import embed as II

args = sys.argv
if len(args) != 2:
    cityname, state = "Raleigh", "North Carolina"
else:
    cityname, state = args[1].split(",")

try:
    with open("apikey.pickle", "rb") as key_file:
        apikey = pickle.load(key_file)
except FileNotFoundError as e:
    sys.exit(
        "apikey.pickle not found. Please create an API key at openweathermap.org and pickle it.")


url = f"http://api.openweathermap.org/data/2.5/forecast?q={cityname},{state}&appid={apikey}"

response = requests.get(url).json()
if response["message"] != 0:
    sys.exit(response["message"])

# get the actual forecasts from response
forecasts = response["list"]


parsed_data = {}
# add forecasted data to a dictionary to be converted to a dataframe
for item in forecasts:
    timestamp = datetime.datetime.fromtimestamp(item["dt"])
    parsed_data[timestamp] = {}
    for key, value in item["main"].items():
        parsed_data[timestamp][key] = value

# create dataframe from parse_data and transpose it
df = pd.DataFrame.from_dict(parsed_data)
df = df.T

# convert temperatures from Kelvin to Celsius
df[["temp", "feels_like", "temp_min", "temp_max"]] = df[[
    "temp", "feels_like", "temp_min", "temp_max"]] - 273.15


def CtoF(x):
    # celsius to fahrenheit
    return x * 1.8 + 32


def FtoC(x):
    # fahrenheit to celsius
    return (x - 32) / 1.8


# plot temperature, feels like and humidity
fig, ax = plt.subplots(1, 1, figsize=(15, 5))

ax.plot(df.index, df["temp"].apply(CtoF),
        "bo-", label="Temperature", alpha=0.5)
ax.plot(df.index, df["feels_like"].apply(CtoF),
        "m^-", label="Feels Like", alpha=0.5)
# share x axis
ax2 = ax.twinx()
ax2.plot(df.index, df["humidity"], "gs-", label="Humidity", alpha=0.5)

# labeling and title
ax.set_ylabel("T [F]", fontsize=14)
ax2.set_ylabel("Relative Humidity [%]", fontsize=14)
ax.set_title(args[1], fontsize=16)

# formatting x axis
ax.set_xticks(df.index)
xlabs = [i.strftime("%a %I %p") for i in df.index]
ax.set_xticklabels(xlabs, rotation=45, ha="right")

# adjust the bottom of the plot to not cut off x labels
plt.subplots_adjust(bottom=0.2)

# adding a legend
fig.legend(loc="upper left")

plt.show()
