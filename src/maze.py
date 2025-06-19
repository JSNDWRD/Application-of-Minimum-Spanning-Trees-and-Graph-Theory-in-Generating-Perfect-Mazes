import numpy as np

def CreateGrid(w,h):
    # w dan h harus ganjil
    if w % 2 == 0:
        w = w+1
    if h % 2 == 0:
        h = h+1
    # return array 2 dimensi dengan tiap elemen bernilai 1
    return np.ones((h,w),dtype=int)

def GetWalls(x,y, grid):
    directions = [(-2,0), (2,0), (0,-2), (0,2)]
    walls = []
    for i,j in directions:
        xf = x+i
        yf = y+j
        if (0 < xf < grid.shape[1]) and (0 < yf < grid.shape[0]) and (grid[xf][yf] == 1):
            xt = x+i // 2
            yt = y+j // 2
            walls.append((xf,yf,xt,yt))
    return walls