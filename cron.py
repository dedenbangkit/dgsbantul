import requests as r
import pandas as pd
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

df.to_csv("data.csv")
