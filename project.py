import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([('bird', 'falcon'), ('bird', 'parrot'), ('mammal', 'lion'), ('mammal', 'monkey')], names=['class', 'name'])
columns = pd.MultiIndex.from_tuples([('speed', 'max'), ('species', 'type')])
df = pd.DataFrame([(389.0, 'fly'), ( 24.0, 'fly'), ( 80.5, 'run'), (np.nan, 'jump')], index=index, columns=columns)

print(df)
print('\n')

df0 = df.reset_index(inplace=True, drop=True )
print(df0)
print('\n')
