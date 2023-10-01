import numpy as np

from data_importer import load_data_3D
from data_transformer import save_vdb

if __name__ == '__main__':
    # import binvox to numpy
    bunny = load_data_3D("bunny.binvox")

    # alternative import directly from numpy array
    bunny = np.load("bunny_256.npy")

    save_vdb(
        data=bunny,
        write_out="bunny_256.vdb"
    )
