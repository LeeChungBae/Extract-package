# src/extract_package/extract.py

import requests
import os
import pandas as pd

SAVE_PATH = '/home/centa/code/team_repo/extract_result'             # relative path from 'team_repo/Airflow_dags'

def get_key():
    key = os.getenv("MOVIE_API_KEY")        # need to add how-to in README
    return key

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    return url 

def req(dt="20120101"):
    url = gen_url(dt)
    r= requests.get(url)
    data = r.json()
    return data

def req2list(dt="20120101"):
    data = req(dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def list2df(dt="20120101"):
    l = req2list(dt)
    df = pd.DataFrame(l)
    return df 

def save2df(dt="20120101", parquet_path=SAVE_PATH):
    df = list2df(dt)
    df['load_dt'] = dt
    return df
