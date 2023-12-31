# Render Numpy to OpenVDB

Convert binvox voxels into numpy array, then using PyOpenVDB, convert from numpy array into VDB format, for import into e.g. Blender.

## Build and install PyOpenVDB dependency

Build and installation instructions for pyopenvdb with use numpy featured enabled.


### MacOS

```
# use virtualenv, e.g. venv

brew install boost
brew install tbb
brew install c-blosc
brew install cmake
brew install pybind11

git clone git@github.com:AcademySoftwareFoundation/openvdb.git
cd openvdb
mkdir build
cd build

# in your virtualenv
pip install numpy

# build with cmake
# the pybind11 path was necessary for me, maybe not for you
# if necessary, ensure path to pybind11 is correct for your installation
cmake .. -D OPENVDB_BUILD_PYTHON_MODULE=ON -D CMAKE_PREFIX_PATH=/usr/local/Cellar/pybind11/2.11.1/share/cmake/pybind11 -D USE_NUMPY=ON

# install with cmake
make -j4
sudo make install

# to make it available in your venv, either symlink or copy the custom binary into venv
# change the second path to the path of your venv installation for your project
cp  /usr/local/lib/python3.9/site-packages/pyopenvdb.cpython-39-darwin.so /Users/wenxinliu/Documents/thesis/render_images/venv/lib/python3.9/site-packages/
```
### Linux

```agsl
# @note If your distribution does not have required versions, consider using
#   apt pinning. See the dependency documentation for more details.
apt-get install -y libboost-iostreams-dev
apt-get install -y libtbb-dev
apt-get install -y libblosc-dev

git clone git@github.com:AcademySoftwareFoundation/openvdb.git
cd openvdb
mkdir build
cd build

# build with cmake
cmake .. -D OPENVDB_BUILD_PYTHON_MODULE=ON -D USE_NUMPY=ON

# install with cmake
make -j4
sudo make install
```
## Run instruction

```agsl
python3 main.py
```
