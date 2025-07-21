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
    dic_Apartment[f'Apartment_{i+1}'] = (row['x'], row['y'])

# Building 좌표
Building = df_merged[df_merged['struct'] == 'Building'].reset_index(drop = True)

dic_Building = {}
for i, row in Building.iterrows():
    if is_Construction(row['x'], row['y']):
        continue
    dic_Building[f'Building_{i+1}'] = (row['x'], row['y'])

# 건설 현장
dic_Construction = {}

Construction = df_merged[df_merged['ConstructionSite'] == 1].reset_index(drop = True)

for i, row in Construction.iterrows():
    dic_Construction[f'Construction_{i+1}'] = (row['x'], row['y'])

#반달곰 커피
dic_BandalgomCoffee = {}

BandalgomCoffee = df_merged[df_merged['struct'] == 'BandalgomCoffee']

for i, (x, y) in enumerate(zip(BandalgomCoffee['x'], BandalgomCoffee['y']), start=1):
    dic_BandalgomCoffee[f'BandalgomCoffee_{i}'] = (x, y)

# 집
MyHome = tuple(df_merged[df_merged['struct'] == 'MyHome'].iloc[0][['x', 'y']].apply(int))

# queue 구현
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

def make_grid(max_x, max_y, obstacles):
    rows, cols = max_y + 1, max_x + 1  # 좌표 최대값 포함하도록 +1 권장
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    obstacle_positions = set()
    for v in obstacles.values():
        obstacle_positions.add(tuple(v))  # set → tuple 변환

    for r in range(rows):
        for c in range(cols):
            if (c, r) in obstacle_positions:
                grid[r][c] = 1

    return grid


def bfs(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    dist = [[-1] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]

    q = Queue()
    sx, sy = start
    gx, gy = goal

    q.enqueue((sx, sy))
    visited[sy][sx] = True
    dist[sy][sx] = 0

    directions = [(-1,0), (1, 0), (0, -1), (0, 1)]

    while not q.is_empty():
        x, y = q.dequeue()

        if (x, y) == (gx, gy):
            break

        for dx, dy in directions:
            nx, ny = x + dx, y+ dy
            if 0 <= ny < rows and 0 <= nx < cols:
                if not visited[ny][nx] and grid[ny][nx] == 0:
                    visited[ny][nx] = True
                    dist[ny][nx] = dist[y][x] + 1
                    prev[ny][nx] = (x,y)
                    q.enqueue((nx, ny))
    
    path = []
    if dist[gy][gx] != -1:
        cur = (gx, gy)
        while cur is not None:
            path.append(cur)
            cur = prev[cur[1]][cur[0]]
        path.reverse()

    return dist[gy][gx], path 

max_x = df_merged['x'].max()
max_y = df_merged['y'].max()

grid = make_grid(max_x, max_y, dic_Construction)       
start=MyHome
goal_1=dic_BandalgomCoffee['BandalgomCoffee_1']
goal_2=dic_BandalgomCoffee['BandalgomCoffee_2']

distance_1, path_1 = bfs(start, goal_1, grid)
distance_2, path_2 = bfs(start, goal_2, grid)

if distance_1 > distance_2:
    min_distance = distance_2
    min_path = path_2
else:
    min_distance = distance_1
    min_path = path_1
print(min_path)

df_path = pd.DataFrame(min_path, columns = ['x', 'y'])
df_path.to_csv('home_to_cafe.csv')

import map_draw
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.patches as patches

fig, ax = map_draw.map_visual(df_merged)
x_vals = [x for x, y in min_path]
y_vals = [y for x, y in min_path]
ax.plot(x_vals, y_vals, color = 'red', linewidth = 3, zorder = 10)
plt.show()
fig.savefig('map_final.png')

