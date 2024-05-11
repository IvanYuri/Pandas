import pandas as pd

df = pd.read_csv('AMZN.csv')

# print(df.to_string())
print(df['Low'].std())

# print(df.std())
