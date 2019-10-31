import pandas as pd

df = pd.read_csv('forestFire.csv')
df.to_json('forestFire.json', orient='records', lines=True)