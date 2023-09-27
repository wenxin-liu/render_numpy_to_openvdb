import pyopenvdb as vdb
import numpy as np


def save_vdb(data, write_out):
    array = data.astype(np.float64)
    # print(array)
    grid = vdb.FloatGrid()
    grid.copyFromArray(array)
    # print(grid)
    grid.name = 'density'
    vdb.write(write_out, grids=[grid])
