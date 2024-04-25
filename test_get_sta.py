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
        status = []
        yuto = BeautifulSoup(requests.get(yuto_URL).content,"html.parser")
        
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
    return(statuses)

print(get_statuses())