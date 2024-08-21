# Import dependencies
import requests
import json
import pandas as pd

from dotenv import load_dotenv
load_dotenv()
import os

if __name__=="__main__":
    url = "https://v6.exchangerate-api.com/v6/dcba8dfe22112028b6d774ef/codes"
    codes = requests.get(url).json()
    codesy = [sublist[1] for sublist in codes['supported_codes']]
    print(codesy)
    result_dict = {sublist[1]: sublist[0] for sublist in codes['supported_codes']}

    print("Hello, welcome to exchange rates")
    while True:
        x = input("please copy/paste a currency from above: ")
        try:
            dollar_url = f"https://v6.exchangerate-api.com/v6/dcba8dfe22112028b6d774ef/latest/{result_dict[x]}"
            data = requests.get(dollar_url).json()
            data_found=True
        except:
            print("this currency doesn\'t exist. Please Try Again")
            data_found=False

        if data_found:
            print(f"this is the conversion rate of {data['base_code']} to US Dollars: {data['conversion_rates']['USD']}")
            use_library = input("Type 'n' to quit or anything else to continue. ")
            if use_library.lower() == 'n':
                break
        else:
            continue

            


    