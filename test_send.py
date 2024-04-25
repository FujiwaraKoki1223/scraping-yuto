import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# from scraping import get_levels
from get_from_spread import Auth, RawData
from test_get import test_get_levels

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Auth

#スプレッドシートへ入力
levels = test_get_levels()
for i in range(len(levels)):
    row = i+3
    level = levels[i].values()
    #技能レベル送信のための設定
    celllist = RawData.range(f"F{row}:AC{row}")
    for n,count in zip(celllist,range(len(celllist))):
        n.value = int(list(level)[count]) if list(level)[count] else ""

    RawData.update_cells(celllist)