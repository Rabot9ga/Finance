import time

import requests
import csv


isin_list =[]
isin_dict = {}

with open('ISIN.csv', newline='') as f:
    reader = csv.reader(f)
    for i in reader:
        isin_list.append(i[0])



url = 'https://api.openfigi.com/v1/mapping'
headers = {'Content-Type':'text/json', 'X-OPENFIGI-APIKEY':'cf5d9538-95e7-4e30-8ae9-980261536b9c' }

for isin in isin_list:
    payload = '[{"idType":"ID_ISIN","idValue":"'+isin+'"}]'
    r = requests.post(url, headers=headers, data=payload)
    isin_dict[isin] = r.json()[0]["data"][0]["ticker"]
    print(isin, r.json()[0]["data"][0]["ticker"])
    time.sleep(2.5)

with open("isin_ticker.csv", "w", newline="") as file:
    field_name= ['ISIN', 'TICKER']
    writer = csv.DictWriter(file, fieldnames=field_name)
    for i in isin_dict:
        writer.writerow({"ISIN":i, 'TICKER':isin_dict[i]})

# isin = "US26614N1028"
# url = 'https://api.openfigi.com/v1/mapping'
# headers = {'Content-Type':'text/json', 'X-OPENFIGI-APIKEY':'cf5d9538-95e7-4e30-8ae9-980261536b9c' }
# payload = '[{"idType":"ID_ISIN","idValue":"'+isin+'"}]'
# r = requests.post(url, headers=headers, data=payload)
# print(r.json())