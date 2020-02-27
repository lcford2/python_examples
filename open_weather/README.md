### Open Weather API Example

This example pulls 5-day 4-hour forecasted weather data from the Open Weather API and then plots temperature, feels like temperature, and humidity. In this example you are exposed to the following libraries:

* `requests` (Pull data from the internet using a URL)
* `pandas` (Data management)
* `matplotlib` (Plotting in a way similar to MATLAB)
* `pickle` (Serialize python objects for storage)
* `datetime` (Dealing with dates)
* `sys` (System module for various uses)
  
To use this example, you will need to go to the [Open Weather website](https://openweathermap.org/api) and create an account. Once you create an account you will need to create an API key for your personal use. After you have the API key, you can create the `apikey.pickle` file needed to run this example using the following code:

```python
apikey = "your API key as a string"
with open("apikey.pickle", "wb") as key_file:
    pickle.dump(apikey, key_file)
```

After you have created this the `apikey.pickle` in the same directory as the `city_temp_forecasts.py` file, you will be able to execute the script with the following command:

```bash
$ python city_temp_forecasts.py ["City Name, State"]
```

In the above command, `"City Name, State"` is an optional argument to the script. If it is not passed, date for Raleigh, North Carolina will be retrieved. If it is passed it should be in the format indicated in the command (with quotes, and comma separated city and state) e.g. `"Raleigh, North Carolina"`, `"San Diego, California"`, `"Austin, Texas"`, etc... 
