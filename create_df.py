import pandas as pd
import numpy as np


df = pd.read_csv("amazon.csv")
df['index'] = ''
i = 0
for d in range(len(df)):
    df['index'][d] = i
    i += 1
print(df.columns)


ratings = pd.DataFrame(columns=['userId', 'productId', 'rating'])
i=0
for ind in df['index']:
    row = df[df['index'] == ind]
    rating = row['rating'].iloc[0]
    users = row['user_id'].iloc[0].split(',')
    for user in users:
        ratings.loc[i]={'userId': user, 'productId': ind, 'rating': rating}
        i+=1

print(ratings)
