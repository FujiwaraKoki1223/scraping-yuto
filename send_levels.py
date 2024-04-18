import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scraping import get_levels
from time import sleep

Auth = "D:\\Documents\\python-study\\source-codes\\scraping-yuto\\practical-day-419513-c8ed7fadd3b5.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Auth
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(Auth, scope)
Client = gspread.authorize(credentials)
SpreadSheet = Client.open_by_url(url="https://docs.google.com/spreadsheets/d/1OW7io-YI3xWS02vnvVkbh9WmPcCDu9heiONxW7eMCaA/edit?usp=sharing")
#TODO:上記のURLを共有済みのシートをgoogle spreadsheetに変更したもののURLに変更
RawData = SpreadSheet.worksheet("PC")

#スプレッドシートへ入力
levels = get_levels()
for i in range(len(levels)):
    row = i+3
    col = 6
    count=0
    level = levels[i].values()
    celllist = RawData.range(f"F{row}:AC{row}")
    for n in celllist:
        n.value = int(list(level)[count]) if list(level)[count] else ""
        count += 1
    RawData.update_cells(celllist)