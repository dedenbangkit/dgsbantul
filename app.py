import pandas as pd
import sys

df = pd.read_csv('data.csv')
results = df[df['NIK'] == int(sys.argv[1])].to_dict('records')[0]

for k in results:
    if k != 'view':
        if sys.argv[2] == "blank":
            print("{}".format(str(results[k]).upper()))
        else:
            print("{}: {}".format(str(k).upper(),str(results[k]).upper()))
