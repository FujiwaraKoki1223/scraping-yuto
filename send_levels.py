import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scraping import get_levels, get_statuses, get_stts

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
statuses = get_statuses()
stts = get_stts()
for i in range(len(levels)):
    row = i+3
    level = levels[i].values()
    #技能レベル送信のための設定
    celllist = RawData.range(f"F{row}:AC{row}")
    for n,count in zip(celllist,range(len(celllist))):
        n.value = int(list(level)[count]) if list(level)[count] else ""
    #サブステ送信のための設定
    celllist_sta = RawData.range(f"AE{row}:AH{row}")
    status = statuses[i].values()
    for n,count in zip(celllist_sta,range(len(celllist_sta))):
        n.value = int(list(status)[count]) if list(status)[count] else ""
    #能力値送信のための設定
    celllist_stt = RawData.range(f"AO{row}:AT{row}")
    stt = stts[i]
    for n,count in zip(celllist_stt,range(len(celllist_stt))):
        n.value = int(stt[count])

    RawData.update_cells(celllist)
    RawData.update_cells(celllist_sta)
    RawData.update_cells(celllist_stt)