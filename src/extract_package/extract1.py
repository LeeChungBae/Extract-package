# src/extract_package/extract.py

import requests
import os
import pandas as pd

SAVE_PATH = '/home/nishtala/code/team_repo/extract_result'

def get_key():
    key = os.getenv("MOVIE_API_KEY")        # need to add how-to in README
    return key

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    return url

def request(dt="20120101"):
    url = gen_url(dt)
    r = requests.get(url)
    data = r.json()
    return data

def save_pq(dt="20120101", parq_path=SAVE_PATH):
    data = request(dt)
    data_list = data['boxOfficeResult']['dailyBoxOfficeList']
    df = pd.DataFrame(data_list)
    df['load_dt'] = dt
    df.to_parquet(parq_path, partition_cols=['load_dt'])
    return df
