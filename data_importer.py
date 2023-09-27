# load binvox data
import binvox_rw
import numpy as np


def load_data_3D(fn):
    with open(fn, 'rb') as fin:
        out = binvox_rw.read_as_3d_array(fin)

        return np.where(np.array(out.data) == True, 1.0, 0.0)