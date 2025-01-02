!pip install gspread oauth2client openai==0.28 google-auth google-auth-oauthlib google-auth-httplib2 pandas --upgrade

import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import pandas as pd
from google.colab import auth
from google.auth import default
import os
import json

# 生成AIを動かす関数を定義
openai.api_key = "<OpenAI API Key>"

def ai(x):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "人間の仕事を助ける優秀なAIアシスタントとして、指示に従い、必要な情報を出力します。出力が長大になっても構わないので、網羅的かつ詳細に出力します。"},
            {"role": "user", "content": x},
        ]
    )
    return response["choices"][0]["message"]["content"]

# Google認証
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

# スプレッドシートとシートを開く
sheet_url = '<URL>'
spreadsheet = gc.open_by_url(sheet_url)

# 各シートを取得
sheet_prot = spreadsheet.worksheet('prot')

# シートからランダムに値を取得
prot_reference= random.choice(sheet_prot.col_values(2)[1:])
print(prot_reference)

# 登場人物の設定を定義

protagonist = """
<主人公の人物像>
"""

SubCharacter = """
<サブキャラクターの人物像>
"""

antagonist = """
<主人公と対立する者の人物像>
"""

# プロットを生成
prot = ai(f"""
下記の資料を元に、物語のプロットを出力してください。プロットの出力形式は、プロットのリファレンスを参考にしてください。
\n主人公の人物像: {protagonist},
\nサブキャラクターの人物像: {SubCharacter},
\n主人公と対立する者の人物像: {antagonist},
\nプロットのリファレンス: {prot_reference},
""")

print(prot)
