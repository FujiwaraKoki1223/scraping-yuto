import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from get_from_spread import get_jobs, get_URLs

levels=[]
statuses=[]
stts=[]
driver_path = f"{os.getcwd()}\\scraping-yuto\\chromedriver.exe"
# brave_path（仮称）にブラウザのパスを入力
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
#TODO:上記の変数名を変更
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
    for i in sheet_jobs:
        all_jobs[i] = ""
    #上の辞書に1レベル以上とっている技能のみ値を代入
    job = ""
    for i in job_levels:
        if job in sheet_jobs:
            all_jobs[job] = i
        job = i
    return all_jobs

#起動するブラウザをBraveに変更
option = webdriver.ChromeOptions()
option.binary_location = brave_path

#headlessモード（ブラウザを表で起動しない）
option.add_argument("--headless")

#chromedriverのパスを指定
service = Service(executable_path=driver_path)

#ゆとしーとへアクセス
yuto = webdriver.Chrome(options=option, service=service)
def get_levels():
    for yuto_URL in yuto_URLs:
        yuto.get(yuto_URL)


        #ゆとしーとの技能レベルを取得して
        jobs = yuto.find_element(by="id", value="classes").text
        #１キャラ分の技能レベルの辞書が要素で、その辞書が全キャラ分入ったリストを作成
        job_levels = list(map(str,jobs.split("\n")))
        levels.append(get_level(job_levels))

        all_statuses = {}
        key = False
        n = 0
        yuto.get(yuto_URL)
        status_data = yuto.find_element(by="id", value="sub-status").text
        status_list = list(map(str,status_data.split("\n")))
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
            stt_data = yuto.find_element(by="id", value=f"stt-{stt}")
            stt_value = int(stt_data.find_element(By.TAG_NAME, "dd").text)
            add_data = yuto.find_element(by="id", value=f"stt-add-{add}")
            add_value_txt = add_data.find_element(By.TAG_NAME, "dd").text
            add_value = int(add_value_txt) if add_value_txt else 0
            all_stts.append(stt_value+add_value)
        stts.append(all_stts)
    return(levels,statuses,stts)
