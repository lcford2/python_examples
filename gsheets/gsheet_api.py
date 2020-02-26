from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import numpy as np
from scipy.stats import norm

# * Everytime you modify the scopes you need to delete the token.pickle file
# Scopes define the permissions
# Can read more about scopes @ https://developers.google.com/sheets/api/guides/authorizing
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# get the id from the url
# * https://docs.google.com/spreadsheets/d/<GSHEET_ID>/edit#gid=0
# TODO: You will need to update this with your own sheet prior to using this code
GSHEET_ID = "1-tQcG0mf7XZTTNdtLXZ24hu-o-NTzPZ0Sh2Ghl6Uy2A"


def get_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def build_service(creds):
    return build('sheets', 'v4', credentials=creds)


def main():
    creds = get_credentials()
    service = build_service(creds)
    loc = 1
    scale_div = 1
    x = np.linspace(norm.ppf(0.01, loc, 1 / scale_div), norm.ppf(
        0.99, loc, 1 / scale_div), 1000).reshape(1000, 1)
    for i in range(1, 10):
        if i == 1:
            x = np.append(x, norm.pdf(x, loc, i / scale_div), axis=1)
        else:
            x = np.append(x, norm.pdf(
                np.linspace(norm.ppf(0.01, loc, i / scale_div), norm.ppf(
                    0.99, loc, i / scale_div), 1000).reshape(1000, 1),
                loc, i / scale_div), axis=1)
    values = x.tolist()
    insert_dict = {
        "values": values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=GSHEET_ID, range="Sheet1!A1:J1000",
        valueInputOption="USER_ENTERED", body=insert_dict).execute()
    print(f"{result.get('updatedCells')} cells updated")


if __name__ == "__main__":
    main()
