# Husk kommando: export IEX_TOKEN=pk_afa0cda4e89a4441845865b55c60dc41



import os
import requests
import pandas as pd

token = os.environ.get('IEX_TOKEN')
base_url = 'https://cloud.iexapis.com/v1'
sandbox_url = 'https://sandbox.iexapis.com/stable/'

stock = input('Enter a stock: ')
option = input('Enter an option: ')



request_data_url = f'{base_url}/stock/{stock}/{option}?token={token}'

print(request_data_url)

respons_data = requests.get(request_data_url).json()

# respons_data.raise_for_status() # This is a built-in function of the requests library. The advantage of this method is that we can log the exception if desired and we can also stop our code from proceeding if the data call was not valid.


