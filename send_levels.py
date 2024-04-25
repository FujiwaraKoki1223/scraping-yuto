import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scraping import get_levels
from get_from_spread import Auth, RawData

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Auth

#スプレッドシートへ入力
levels,statuses,stts = get_levels()
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