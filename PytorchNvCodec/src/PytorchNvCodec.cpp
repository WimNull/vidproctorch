/*
 * Copyright 2020 NVIDIA Corporation
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *    http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <cuda.h>
#include <cuda_runtime.h>
#include <torch/extension.h>

torch::Tensor makefromDevicePtrUint8(CUdeviceptr ptr, uint32_t width,
                                     uint32_t height, uint32_t pitch,
                                     uint32_t elem_size_bytes, size_t str = 0U)
{
  if (elem_size_bytes != 1) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << ": only torch::kUInt8 data type is supported";
    throw std::runtime_error(ss.str());
  }

  auto options = torch::TensorOptions()
                     .dtype(torch::kUInt8)
                     .layout(torch::kStrided)
                     .device(torch::kCUDA);

  torch::Tensor tensor = torch::full({height, width}, 128, options);

  uint8_t* devMem = nullptr;
  try {
    devMem = tensor.data_ptr<uint8_t>();
  } catch (std::exception& e) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << " failed to obtain uint8_t data pointer: " << e.what();
    throw std::runtime_error(ss.str());
  }

  if (!ptr) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << ": Video frame has void CUDA device ptr.";

    throw std::runtime_error(ss.str());
  }

  auto res = str ? cudaMemcpy2DAsync(
                       (void*)devMem, width, (const void*)ptr, pitch, width,
                       height, cudaMemcpyDeviceToDevice, (cudaStream_t)str)
                 : cudaMemcpy2D((void*)devMem, width, (const void*)ptr, pitch,
                                width, height, cudaMemcpyDeviceToDevice);
  if (cudaSuccess != res) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << ": failed to copy data to tensor. CUDA error code: ";
    ss << res;

    throw std::runtime_error(ss.str());
  }

  return tensor;
}

void copytoDevicePtrUint8(torch::Tensor tensor, CUdeviceptr ptr, uint32_t width,
                          uint32_t height, uint32_t pitch,
                          uint32_t elem_size_bytes, size_t str = 0U)
{
  if (elem_size_bytes != 1) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << ": only torch::kUInt8 data type is supported";
    throw std::runtime_error(ss.str());
  }

  uint8_t* devMem = nullptr;
  try {
    devMem = tensor.data_ptr<uint8_t>();
  } catch (std::exception& e) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << " failed to obtain uint8_t data pointer: " << e.what();
    throw std::runtime_error(ss.str());
  }

  if (!devMem) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << ": Pytorch tensor doesn't have data ptr.";

    throw std::runtime_error(ss.str());
  }

  if (!ptr) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << ": Video frame has void CUDA device ptr.";

    throw std::runtime_error(ss.str());
  }

  auto res = str ? cudaMemcpy2DAsync(
                       (void*)ptr, pitch, (const void*)devMem, width, width,
                       height, cudaMemcpyDeviceToDevice, (cudaStream_t)str)
                 : cudaMemcpy2D((void*)ptr, pitch, (const void*)devMem, width,
                                width, height, cudaMemcpyDeviceToDevice);
  if (cudaSuccess != res) {
    std::stringstream ss;
    ss << __FUNCTION__;
    ss << ": failed to copy data to tensor. CUDA error code: ";
    ss << res;

    throw std::runtime_error(ss.str());
  }
}

PYBIND11_MODULE(LibPytorchNvCodec, m)
{
  m.def(
      "makefromDevicePtrUint8",
      [](CUdeviceptr ptr, uint32_t width, uint32_t height, uint32_t pitch,
         uint32_t elem_size_bytes, size_t str) {
        return makefromDevicePtrUint8(ptr, width, height, pitch,
                                      elem_size_bytes, str);
      },
      py::return_value_policy::move);
  m.def(
      "DptrToTensor",
      [](CUdeviceptr ptr, uint32_t width, uint32_t height, uint32_t pitch,
         uint32_t elem_size_bytes, size_t str) {
        return makefromDevicePtrUint8(ptr, width, height, pitch,
                                      elem_size_bytes, str);
      },
      py::return_value_policy::move);
  m.def(
      "makefromDevicePtrUint8",
      [](CUdeviceptr ptr, uint32_t width, uint32_t height, uint32_t pitch,
         uint32_t elem_size_bytes) {
        return makefromDevicePtrUint8(ptr, width, height, pitch,
                                      elem_size_bytes);
      },
      py::return_value_policy::move);
  m.def(
      "DptrToTensor",
      [](CUdeviceptr ptr, uint32_t width, uint32_t height, uint32_t pitch,
         uint32_t elem_size_bytes) {
        return makefromDevicePtrUint8(ptr, width, height, pitch,
                                      elem_size_bytes);
      },
      py::return_value_policy::move);
  m.def("TensorToDptr", [](torch::Tensor& tensor, CUdeviceptr ptr,
                           uint32_t width, uint32_t height, uint32_t pitch,
                           uint32_t elem_size_bytes, size_t str) {
    return copytoDevicePtrUint8(tensor, ptr, width, height, pitch,
                                elem_size_bytes, str);
  });
  m.def("TensorToDptr",
        [](torch::Tensor& tensor, CUdeviceptr ptr, uint32_t width,
           uint32_t height, uint32_t pitch, uint32_t elem_size_bytes) {
          return copytoDevicePtrUint8(tensor, ptr, width, height, pitch,
                                      elem_size_bytes);
        });
}
