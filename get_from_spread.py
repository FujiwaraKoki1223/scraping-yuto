import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from env import RawData

def get_jobs():
    val = RawData.get("F1:AC1")[0]
    return(val)

def get_URLs():
    val = RawData.get("A3:A14")
    URL = []
    for i in val:
        URL.append(i[0])
    return(URL)
print(get_URLs())