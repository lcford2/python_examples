### Google sheets Python API

This is an example of how to push data to a google sheet with python. This example is rather trivial, but this can be useful for many other applications. For example, I use this API to look at results from model runs on an HPC cluster. The data is automatically pushed to a Google Sheet and the plots on that sheet automatically update. This way I can view the results without having access to the cluster. 

You will need to install several packages to run this. I created an environment specifically for interacting with google sheets but you can install these packages in whatever environment you please. 

To install all the requisite packages and create a new environment, use `conda env create -f google-api-env.yml`.

There are also a few steps that you will need to complete before using this example. 

1. Go to this [website](https://developers.google.com/sheets/api/quickstart/python) and follow the instructions for activating the Google Sheets API. 
2. Move the `credentials.json` file into the same folder as the `gheet_api.py` file
3. Create a Google Sheet that you want to update with this example. 
4. Copy the ID of that sheet and set the variable `GSHEET_ID` in `gsheet_api.py` to that ID.
    * The ID can be found in the URL (e.g. https://docs.google.com/spreadsheets/d/<GSHEET_ID>/edit#gid=0)
5. Run the Python file: `python gsheet_api.py` from within the environment that has your API packages. 

This example is adapted from the [Google Developers Tutorial](https://developers.google.com/sheets/api/quickstart/python)