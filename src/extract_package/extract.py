# src/extract_package/extract.py

import requests
import os
import pandas as pd

SAVE_PATH = '../extract_result'             # relative path from 'team_repo/Airflow_dags'

def get_key():
    key = os.getenv("MOVIE_API_KEY")        # need to add how-to in README
    return key

def gen_url(dt="20120101", url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

## continue next tim1!!!
