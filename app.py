import pandas as pd
import requests as r
import sys
import os

if (len(sys.argv) == 4):
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
    df["alamat_lengkap"] = df["desa"] + ", " + df["dusun"] + ", " + df["alamat"]
    df.to_csv('data.csv')

df = pd.read_csv('data.csv')
df["NIK"] = df["NIK"].fillna(0).astype(int)
df["kd_pasien"] = df["kd_pasien"].fillna(0).astype(int)
results = df[df['NIK'] == int(sys.argv[1])].to_dict('records')[0]

for k in results:
    if k != 'view':
        if sys.argv[2] == "blank":
            print("{}".format(str(results[k]).upper()))
        elif sys.argv[2] == "selected":
            if k in ["NIK","nama","alamat_lengkap","kd_pasien"]:
                print("{}".format(str(results[k]).upper()))
        else:
            print("{}: {}".format(str(k).upper(),str(results[k]).upper()))
