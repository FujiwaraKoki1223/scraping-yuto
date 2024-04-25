import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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


def get_statuses():
    for yuto_URL in yuto_URLs:
        stt = []
        yuto = BeautifulSoup(requests.get(yuto_URL).content,"html.parser")


        all_stts = []
        for stt,add in zip(["dex", "agi", "str", "vit", "int", "mnd"], ["A", "B", "C", "D", "E", "F"]):
            stt_data = yuto.find(id=f"stt-{stt}")
            stt_value = int(stt_data.find("dd").text)
            add_data = yuto.find(id=f"stt-add-{add}")
            add_value_txt = add_data.find("dd").text
            add_value = int(add_value_txt) if add_value_txt else 0
            all_stts.append(stt_value+add_value)
        stts.append(all_stts)
    return(stts)
print(get_statuses())