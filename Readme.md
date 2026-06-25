身内向けのアプリです
利用時は、環境変数を私までリクエストしてください。

# 使い方

1.
__https://docs.google.com/spreadsheets/d/14lQd9U6Yrsa_D0h6MRkmenUjXkLVDvYyRUO3vsi1KBU/edit#gid=784301881__ にアクセスしてスプレッドシートをコピーする.

2.
さっきコピーして作ったスプレッドシートの1列目と2列目に名前（任意）とゆとしーとのキャラシのURLを入力する.

3.
env.pyを開いて中にある「SpreadSheet = 」の行の「url="__page's URL__"」のpage's URLをさっき1でコピーして作ったスプレッドシートのURLに置き換える.

4.
venvファイルを削除

5.
`python3 -m venv 任意のファイル名`
を実行

6.
windowsなら
`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force`
で設定を緩くした後、
`.\venv\Scripts\Activate.ps1`
などでActivate.ps1を実行

macなら
`.\venv\Scripts\Activate.ps1`
などでActivate.ps1を実行だけ

7.
`pip install -r requirements.txt`
を実行

8.
send_levels.pyを実行
