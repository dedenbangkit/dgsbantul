import requests as r
import pandas as pd
import sys
import os

website = "https://dgskesehatan.bantulkab.go.id/v2"
identity = os.environ["USERNAME"]
password = os.environ["PASSWORD"]
payload = {"identity":identity,"password":password}
session = r.Session()
login = "{}/login".format(website)
session.post(login, data=payload)
registration_data_url = "{}/pasien/get_pasien_json".format(website)
data = session.get(registration_data_url).json().get('data')
df = pd.DataFrame(data)
results = df[df['NIK'] == str(sys.argv[1])].to_dict('records')[0]

for k in results:
    if k != 'view':
        if sys.argv[2] == "blank":
            print("{}".format(results[k].upper()))
        else:
            print("{}: {}".format(k.upper(),results[k].upper()))
