import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

Auth = f"{os.getcwd()}/scraping-yuto/practical-day-419513-c8ed7fadd3b5.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Auth
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(Auth, scope)
Client = gspread.authorize(credentials)

SpreadSheet = Client.open_by_url(url="https://docs.google.com/spreadsheets/d/1OW7io-YI3xWS02vnvVkbh9WmPcCDu9heiONxW7eMCaA/edit?usp=sharing")
#TODO:上記のURLを共有済みのシートをgoogle spreadsheetに変更したもののURLに変更
RawData = SpreadSheet.worksheet("PC")

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