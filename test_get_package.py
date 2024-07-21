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

        yuto = BeautifulSoup(requests.get("https://yutorize.2-d.jp/ytsheet/sw2.5/?id=Lw2aoY").content,"html.parser")
        # yuto = BeautifulSoup(requests.get(yuto_URL).content,"html.parser")

        #判定パッケージを取得
        packages = []
        package = yuto.find(id="package").find_all("tbody")
        for i in package:
            test=package[1].find("tr").find("td")
            packages.append(test)
        print(packages)

get_levels()