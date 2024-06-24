import os
from get_from_spread import get_jobs, get_URLs
import requests
from bs4 import BeautifulSoup
from html_to_flat import html_to_flat_array


levels=[]
statuses=[]
stts=[]
# yuto_URL にキャラシの閲覧画面のURLを入力
yuto_URLs = get_URLs()
sheet_URL = "https://docs.google.com/spreadsheets/d/1enSgbWoK6kDz-eltbRQ9V4iRHfPD6DV_m2s3qyYcsHc/edit#gid=654293144"
#TODO:上記のURLを本物のPC管理に変更する
#スプレッドシートから技能一覧を取得（本体は別ファイル）
sheet_jobs = get_jobs()

#ゆとしーとから技能レベルを取得する関数
def get_level(job_levels):
    #シート順の技能一覧がインデックスで値が空欄の辞書を作成
    all_jobs ={}
    flag_pri=False
    for i in sheet_jobs:
        all_jobs[i] = ""
    #上の辞書に1レベル以上とっている技能のみ値を代入
    job = ""
    for i in job_levels:
        #プリは信仰が記されてるので対応
        if job == "プリースト":
            flag_pri=True
        elif flag_pri:
            all_jobs["プリースト"] = i
            flag_pri=False
        elif job in sheet_jobs:
            all_jobs[job] = i
        job = i
    return all_jobs

#ゆとしーとへアクセス
def get_levels():
    for yuto_URL in yuto_URLs:
        level = []
        yuto = BeautifulSoup(requests.get(yuto_URL).content,"html.parser")
        #ゆとしーとの技能レベルを取得して
        jobs = yuto.find(id="classes")
        html_to_flat_array(jobs, level)
        levels.append(get_level(level))

        all_statuses = {}
        key = False
        n = 0
        status_data = yuto.find(id="sub-status").text
        status_list = list(map(str,status_data.split("\n")))
        status_list = list(filter(None, list(i.strip() for i in status_list)))
        for i in status_list:
            if n % 2 == 1:
                x = i[i.find("=")+1:]
                if x == "なし":
                    x = ""
                all_statuses[key] = x
            key = i
            n += 1
        statuses.append(all_statuses)

        all_stts = []
        for stt,add in zip(["dex", "agi", "str", "vit", "int", "mnd"], ["A", "B", "C", "D", "E", "F"]):
            stt_data = yuto.find(id=f"stt-{stt}")
            stt_value = int(stt_data.find("dd").text)
            add_data = yuto.find(id=f"stt-add-{add}")
            add_value_txt = add_data.find("dd").text
            add_value = int(add_value_txt) if add_value_txt else 0
            all_stts.append(stt_value+add_value)
        stts.append(all_stts)
    return(levels,statuses,stts)
