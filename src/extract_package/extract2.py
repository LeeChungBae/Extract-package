import requests
import os
import pandas as pd

SAVE_PATH = "/home/joo/code/team_repo/data/extract_result"

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key
		
def gen_url(dt="20230501"):  
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    return url
    
def request(dt="20230501"):
    url = gen_url(dt)
    r = requests.get(url)
    data = r.json()
    return data

def save_parquet(dt='20230501', parq_path=SAVE_PATH):
    data = request(dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    df = pd.DataFrame(l)
    df['load_dt'] = dt
    df.to_parquet(parq_path, partition_cols=['load_dt'])
    return df
