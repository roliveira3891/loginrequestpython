import requests
from bs4 import BeautifulSoup
from busca.seach import filter_error
from busca.login import login_data
from busca.headers import header
from dotenv import load_dotenv
from database.connection import dataExecute
import os
load_dotenv()

with requests.Session() as s:

    #login
    url = os.getenv('URL_LOGIN')
    r = s.post(url, data=login_data(), headers=header())
    data = r.json()
    token = data['token']

    #print(token)
    
    #seach data

    url = os.getenv('URL_SEACH')+filter_error(token)
    print('Seach Errors')
    print('------------')
    #print(url)
    r = s.get(url, headers=header())
    data = r.json()
    #print(r.content)

    items = data['data'][0]['values']
    for item in items:
        qos_unique_user = item['qos_unique_user']
        error_player_code = item['error_player_code']
     
        print(qos_unique_user)
        print(error_player_code)
        print('---')     

   

    

    