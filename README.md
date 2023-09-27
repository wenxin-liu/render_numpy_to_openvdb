Convert voxels into numpy array, then into VDB format, for import into Blender.


build and installation instructions for pyopenvdb with numpy enabled, on macos

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
cmake .. -D OPENVDB_BUILD_PYTHON_MODULE=ON -DCMAKE_PREFIX_PATH=/usr/local/Cellar/pybind11/2.11.1/share/cmake/pybind11 -D USE_NUMPY=ON

# install with cmake
make -j4
sudo make install

# to make it available in your venv, either symlink or copy the custom binary into venv
# change the second path to the path of your venv installation for your project
cp  /usr/local/lib/python3.9/site-packages/pyopenvdb.cpython-39-darwin.so /Users/wenxinliu/Documents/thesis/render_images/venv/lib/python3.9/site-packages/
```

To use:

```agsl
python3 main.py
```