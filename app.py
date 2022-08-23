import pandas as pd
import numpy as np

df = pd.read_csv('testdata.csv')
df = df.filter(['Unique Sector ID', 'Raw Position', 'Improved Position', 'Number Improved Position Entries'])

df['latitude'],df['longitude'] = np.where(
                                    df['Number Improved Position Entries'] >= 1, 
                                    (   
                                        df['Improved Position'].str.split(';').str[0].str.slice(2), 
                                        df['Improved Position'].str.split(';').str[1].str.slice(2)
                                    ), 
                                    (   
                                        df['Raw Position'].str.split(';').str[0].str.slice(2), 
                                        df['Raw Position'].str.split(';').str[1].str.slice(2)
                                    ))

df = df.drop(columns=['Raw Position', 'Improved Position', 'Number Improved Position Entries'])

df.to_csv('result.csv', encoding='utf-8')
