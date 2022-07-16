# VideoProcessingFramework

## Install

1. Prepare
[Video_Codec_SDK](https://developer.nvidia.com/nvidia-video-codec-sdk)
```
# the basics
sudo apt-get update
cmake>=3.21    小于可能会报错
```
cd cmake-3.21*
sudo apt-get install libssl-dev
export CMAKE_CXX_STANDARD=11
./bootstrap --parallel=32
make -j32
sudo make install -j32
sudo ln -s /usr/local/bin/cmake /usr/bin/cmake
cmake --version
```
sudo apt-get install build-essential 
pip install pybind11
```
2. compile
mkdir -p build 
cd build
cmake -D GENERATE_PYTORCH_EXTENSION:BOOL="1"  ..
make -j32
make install

3. install
**复制共享库:** 
```
sudo cp Video_Codec_SDK/Lib/linux/stubs/x86_64/* /usr/local/cuda/lib64/
cd /usr/local/cuda/lib64/
sudo ln -s libnvcuvid.so libnvcuvid.so.1
sudo ln -s libnvidia-encode.so libnvidia-encode.so.1
```
python setup.py bdist_wheel
python setupnvtorch.py bdist_wheel
unzip -l dist/PyNvCodec-0.2.0-py3-none-any.whl
unzip -l dist/PytorchNvCodec-0.2.0-py3-none-any.whl
pip install dist/PyNvCodec-0.2.0-py3-none-any.whl
pip install dist/PytorchNvCodec-0.2.0-py3-none-any.whl

rm -rf PyNvCodec.egg-info PytorchNvCodec.egg-info build dist


sudo ln -sf  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.1.0  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8
sudo ln -sf  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.1.0  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8
sudo ln -sf  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.1.0  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8
sudo ln -sf  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.1.0  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8
sudo ln -sf  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_ops_train.so.8.1.0  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_ops_train.so.8
sudo ln -sf  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.1.0  /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn_adv_train.so.8