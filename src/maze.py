import numpy as np

def CreateGrid(w,h):
    # w dan h harus ganjil
    if w % 2 == 0:
        w = w+1
    if h % 2 == 0:
        h = h+1
    return np.ones((h,w),dtype=int)

x = CreateGrid(25,25)
print(x)