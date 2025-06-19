import numpy as np
import random
import matplotlib.pyplot as plt
from collections import deque

# Inisialisasi maze dalam format array 2 dimensi
def CreateGrid(w,h):
    # return array 2 dimensi dengan tiap elemen bernilai 1
    return np.ones((h,w),dtype=int)

# Mencari dan mengembalikan daftar koordinat potensial beserta koordinat di antaranya dengan koordinat (x,y) yang dapat dijadikan sebagai lintasan
def GetWalls(x,y, grid):
    directions = [(-2,0), (2,0), (0,-2), (0,2)]
    walls = []
    for i,j in directions:
        xf = x+i # koordinat adjacent 2 langkah
        yf = y+j
        if (0 < xf < grid.shape[1]) and (0 < yf < grid.shape[0]) and (grid[yf][xf] == 1):
            xt = x+i // 2 # koordinat di antara adjacent dengan (x,y)
            yt = y+j // 2
            walls.append((xf,yf,xt,yt))
    return walls

# Generate maze secara random
def GenerateMaze(w,h):
    grid = CreateGrid(w, h) # Inisialisasi maze
    xs = random.randrange(1, w, 2) # Ambil value random ganjil di antara 1 sampai w-1
    ys = random.randrange(1, h, 2) # 1, 3, 5, ..., h-1
    grid[ys][xs] = 0 # Titik awal maze generation
    walls = GetWalls(xs, ys, grid) # Mengambil koordinat yang adjacent 2 langkah dengan titik awal

    # Ambil koordinat wall dalam list secara random selama list belum kosong
    while walls:
        x1, y1, x2, y2 = wall = random.choice(walls)
        walls.remove(wall)
        if grid[y1][x1] == 1:
            grid[y1][x1] = 0
            grid[y2][x2] = 0
            walls.extend(GetWalls(x1,y1,grid)) # tambahkan koordinat yang adjacent 2 langkah dengan koordinat (x1,y1)
    
    grid[0][1] = 0 # Entrance di kiri atas
    entrance = (1,0)
    grid[h-1][w-2] = 0
    exit = (w-2,h-1) # Exit di kanan bawah

    return grid, entrance, exit

# Menggunakan pendekatan BFS untuk mencari jalan keluar dari maze
def SolveMaze(maze, entrance, exit):
    start = (entrance[1], entrance[0]) # format (y,x)
    end = (exit[1], exit[0])

    queue = deque([(start, [start])]) # queue berisikan tuple dari koordinat dan lintasan untuk mencapainya
    visited = set([start]) # set dari koordinat yang sudah dikunjungi
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # selama queue belum kosong, ambil posisi selanjutnya dan lintasan dari depan queue
    while queue:
        (y,x), path = queue.popleft()
        if(x,y) == (end[1], end[0]): # Titik exit
            return [(p[1], p[0]) for p in path] # Mengembalikan list dari koordinat lintasan dari entrance sampai exit

        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if(0 <= nx < maze.shape[1]) and (0 <= ny < maze.shape[0]) and (maze[ny][nx] == 0) and ((ny,nx) not in visited):
                visited.add((ny,nx))
                queue.append(((ny,nx), path + [(ny, nx)]))
    
    return None

# Menampilkan maze dengan PyPlot dalam library Matplotlib
def PlotMaze(maze):
    plt.figure(figsize=(10,10))
    plt.imshow(maze, cmap='binary')
    plt.axis('off')
    plt.title('Perfect Maze')
    plt.show()

# Menampilkan maze beserta dengan solusi jalan keluarnya
def PlotSolvedMaze(maze, path=None):
    plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap='binary')
    
    if path:
        h, w = maze.shape

        yc, xc = zip(*[(y, x) for (x, y) in path])
        plt.plot(xc, yc, color='red', linewidth=4)

    plt.axis('off')
    plt.title('Perfect Maze with Solution')
    plt.show()

# Mengkombinasikan seluruh fungsi
def ShowMaze():
    l = int(input("Masukkan lebar maze: "))
    p = int(input("Masukkan panjang maze: "))
    # Memastikan kedua bilangan adalah ganjil
    if l % 2 == 0:
        l = l + 1
    if p % 2 == 0:
        p = p + 1
    maze, entrance, exit = GenerateMaze(p,l)
    path = SolveMaze(maze, entrance, exit)
    PlotMaze(maze)
    PlotSolvedMaze(maze, path)

# Eksekusi ketika file ini di-run
if __name__ == "__main__":
    ShowMaze()