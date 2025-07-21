
import pandas as pd

# 데이터 불러오기
df_struct = pd.read_csv('area_struct.csv')
df_map = pd.read_csv('area_map.csv')
df_category = pd.read_csv('area_category.csv')

# 열 이름 공백 제거
df_struct.columns = df_struct.columns.str.strip()
df_map.columns = df_map.columns.str.strip()
df_category.columns = df_category.columns.str.strip()

# df_struct의 category를 df_category를 통해 이름 변경(구조물이 없는 경우 None)

df_struct = df_struct.merge(df_category, on = 'category', how = 'left')
df_struct['struct'].fillna('None', inplace = True)
df_struct.drop('category', axis = 1, inplace = True)

# df_struct와 df_map 병합
df_merged = pd.merge(df_struct, df_map, on = ['x', 'y'], how='left')

# area를 기준으로 정렬
df_merged.sort_values(by = 'area', inplace = True)
print(df_merged)
df_merged['struct'] = df_merged['struct'].str.strip() # 구조물 이름 공백 제거

# area 1 필터링 출력
print(df_merged[df_merged['area'] == 1])

df_merged.to_csv('df_merged.csv', index=False)
