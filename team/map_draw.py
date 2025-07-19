import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.patches as patches

df_merged=pd.read_csv('df_merged.csv')

construction_coords = df_merged[df_merged['ConstructionSite'] == 1][['x','y']].values
construction_set = set((x, y) for x, y in construction_coords)

def is_construction(x, y):
    for x_c, y_c in construction_coords:
        if x_c == x and y_c == y:
            return True
    return False



def map(df):
    max_x = df['x'].max()
    max_y = df['y'].max()

    fig, ax = plt.subplots(figsize = (10, 10))
    ax.set_xlim(0.5, max_x + 0.5)
    ax.set_ylim(max_y + 0.5, 0.5)
    ax.set_xticks(range(1, max_x+1))
    ax.set_yticks(range(max_y+1, 0, -1))
    ax.grid(which='both', color='gray', linestyle='--', linewidth=0.5)

    # Apartment, Building
    for struct_type in ['Apartment', 'Building']:
        subset = df[df['struct'] == struct_type]
        for i, row in subset.iterrows():
            x, y = row['x'], row['y']
            if is_construction(x, y):
                continue
            ax.plot(x, y, 'o', color='brown', markersize=20)

    # BandalgomCoffee
    subset = df[df['struct'] == 'BandalgomCoffee']
    for i, row in subset.iterrows():
        x, y = row['x'], row['y']
        if is_construction(x, y):
            continue
        ax.add_patch(
            patches.Rectangle(
                xy=(x-0.3, y-0.3),
                width=0.6,
                height=0.6,
                color='green',
                alpha=0.8
            )
        )

    # MyHome
    subset = df[df['struct'] == 'MyHome']
    for i, row in subset.iterrows():
        x, y = row['x'], row['y']
        if is_construction(x, y):
            continue
    ax.plot(x, y, '^', color='green', markersize=20)
    # 건설 현장
    for _, row in df[df['ConstructionSite'] == 1].iterrows():
        x, y = row['x'], row['y']
        ax.add_patch(
            patches.Rectangle(
                xy=(x-0.3, y-0.3),
                width=0.6,
                height=0.6,
                color='gray',
                alpha=0.8
            )
        )
    # 범례
    legend_handles = [
    lines.Line2D([], [], color='brown', marker='o', linestyle='None', markersize=10, label='Apartment/Building'),  # 원형
    patches.Rectangle((0, 0), 1, 1, facecolor='green', edgecolor='none', label='Bandalgom Coffee'),  # 녹색 사각형
    lines.Line2D([], [], color='green', marker='^', linestyle='None', markersize=10, label='My Home'),  # 삼각형
    patches.Rectangle((0, 0), 1, 1, facecolor='gray', edgecolor='none', label='Construction Site')  # 회색 사각형
    ]

    ax.legend(handles=legend_handles, loc='upper left')

    plt.savefig('map.png')
    plt.show()


map(df_merged)
