import pandas as pd

df_merged = pd.read_csv('df_merged.csv')

Construction_coords = df_merged[df_merged['ConstructionSite'] == 1][['x','y']].values

def is_Construction(x, y):
    for x_c, y_c in Construction_coords:
        if x_c == x and y_c == y:
            return True
    return False

# Apartment 좌표
Apartment = df_merged[df_merged['struct'] == 'Apartment'].reset_index(drop = True)

dic_Apartment = {}
for i, row in Apartment.iterrows():
    if is_Construction(row['x'], row['y']):
        continue
    dic_Apartment[f'Apartment_{i+1}'] = {row['x'], row['y']}

# Building 좌표
Building = df_merged[df_merged['struct'] == 'Building'].reset_index(drop = True)

dic_Building = {}
for i, row in Building.iterrows():
    if is_Construction(row['x'], row['y']):
        continue
    dic_Building[f'Building_{i+1}'] = {row['x'], row['y']}

# 건설 현장
dic_Construction = {}

Construction = df_merged[df_merged['ConstructionSite'] == 1].reset_index(drop = True)

for i, row in Construction.iterrows():
    dic_Construction[f'Construction_{i+1}'] = {row['x'], row['y']}

print(dic_Construction)

#반달곰 커피
dic_BandalgomCoffee = {}

BandalgomCoffee = df_merged[df_merged['struct'] == 'BandalgomCoffee']

for i, (x, y) in enumerate(zip(BandalgomCoffee['x'], BandalgomCoffee['y']), start=1):
    dic_BandalgomCoffee[f'BandalgomCoffee_{i}'] = (x, y)

# 집
MyHome = tuple(df_merged[df_merged['struct'] == 'MyHome'].iloc[0][['x', 'y']].apply(int))

