import pandas as pd
import sys

df = pd.read_csv('data.csv')
results = df[df['NIK'] == str(sys.argv[1])].to_dict('records')[0]

for k in results:
    if k != 'view':
        if sys.argv[2] == "blank":
            print("{}".format(results[k].upper()))
        else:
            print("{}: {}".format(k.upper(),results[k].upper()))
