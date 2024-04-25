import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

Auth = f"{os.getcwd()}/scraping-yuto/practical-day-419513-c8ed7fadd3b5.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Auth
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(Auth, scope)
Client = gspread.authorize(credentials)

# 下の「url="~"」の~にスプレッドシートのURLを入力
SpreadSheet = Client.open_by_url(url="https://docs.google.com/spreadsheets/d/1OW7io-YI3xWS02vnvVkbh9WmPcCDu9heiONxW7eMCaA/edit?usp=sharing")

RawData = SpreadSheet.worksheet("PC")