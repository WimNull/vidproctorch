#
# Copyright 2019 NVIDIA Corporation
# Copyright 2021 Kognia Sports Intelligence
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

cmake_minimum_required(VERSION 3.10)

project(Video_Processing_Framework)

set(TRACK_TOKEN_ALLOCATIONS FALSE CACHE BOOL "Debug memory allocations within VPF")

if(TRACK_TOKEN_ALLOCATIONS)
	add_definitions(-DTRACK_TOKEN_ALLOCATIONS)
endif(TRACK_TOKEN_ALLOCATIONS)

set (CMAKE_CXX_STANDARD 11)
set (VIDEO_CODEC_SDK "${CMAKE_CURRENT_SOURCE_DIR}/Video_Codec_SDK")
set (VIDEO_CODEC_SDK_DIR "${VIDEO_CODEC_SDK}")
set (VIDEO_CODEC_SDK_INCLUDE_DIR "${VIDEO_CODEC_SDK}/Interface")
# message(STATUS "VIDEO_CODEC_SDK_INCLUDE_DIR path: ${VIDEO_CODEC_SDK_INCLUDE_DIR}")
set (NVCUVID_LIBRARY "${VIDEO_CODEC_SDK}/Lib/linux/stubs/x86_64/libnvcuvid.so")
set (NVENCODE_LIBRARY "${VIDEO_CODEC_SDK}/Lib/linux/stubs/x86_64/libnvidia-encode.so")

include_directories(/usr/local/cuda/include)
link_directories(/usr/local/cuda/lib64 /usr/local/nvidia/) 
include_directories(${VIDEO_CODEC_SDK}/Interface)

EXECUTE_PROCESS(COMMAND which python OUTPUT_VARIABLE PYTHON_BINARY)
EXECUTE_PROCESS(COMMAND python -c "import site; print(site.getsitepackages()[0], end='')" OUTPUT_VARIABLE PythonSiteDir)
get_filename_component(PythonDir "${PYTHON_BINARY}" DIRECTORY)
get_filename_component(PythonDir "${PythonDir}" DIRECTORY)
string(STRIP "${MYVAR}" MYVAR_PARSED)
if (PythonDir MATCHES ".*miniconda.*")
    message(STATUS "Python path: ${PythonDir}")
    set(PYTHON_INCLUDE_DIRS "${PythonDir}/include")
    set(PYTHON_LIBRARY_DIR "${PythonDir}/lib")
    link_directories("${PYTHON_LIBRARY_DIR}")
    EXECUTE_PROCESS(COMMAND python -c "import sys; print(sys.version_info.minor, end='')" OUTPUT_VARIABLE PythonVer)
    set(PYTHON_LIBRARIES "${PYTHON_LIBRARY_DIR}/libpython3.${PythonVer}.so")
else ()
    FIND_PACKAGE(PythonLibs 3 REQUIRED)
endif ()
message(STATUS "PYTHON_INCLUDE_DIRS ${PYTHON_INCLUDE_DIRS}, PYTHON_LIBRARIES ${PYTHON_LIBRARIES} ${PYTHON_BINARY}")


add_subdirectory(PyNvCodec)
add_subdirectory(PytorchNvCodec)

include_directories(${TC_CORE_INC_PATH})
include_directories(${TC_INC_PATH})
include_directories(${VIDEO_CODEC_SDK_INCLUDE_DIR})


EXECUTE_PROCESS(COMMAND ${PYTHON_EXECUTABLE} -c "import site; print(site.getsitepackages()[0], end='')"
                OUTPUT_VARIABLE Python3_USER_SITE_DIR)

#Bring all the stuff together
install(FILES $<TARGET_FILE:TC_CORE> DESTINATION "${CMAKE_CURRENT_SOURCE_DIR}/PyNvCodec")
install(FILES $<TARGET_FILE:TC> DESTINATION "${CMAKE_CURRENT_SOURCE_DIR}/PyNvCodec")
install(FILES $<TARGET_FILE:LibPyNvCodec> DESTINATION "${CMAKE_CURRENT_SOURCE_DIR}/PyNvCodec")


if(GENERATE_PYTORCH_EXTENSION)
	#Extension will be built using torch.utils.cpp_extension;
	#So we just launch python script;
	add_custom_command(OUTPUT Pytorch_Nv_Codec
						COMMAND cd ${PYTORCH_EXTENSION_SOURCES_DIR} && python setup.py build --build-lib="${CMAKE_CURRENT_SOURCE_DIR}/PytorchNvCodec")
    add_custom_target(LibPytorchNvCodec DEPENDS Pytorch_Nv_Codec)
    add_dependencies(LibPyNvCodec LibPytorchNvCodec)
    message(STATUS "PYTORCH_EXTENSION_SOURCES_DIR ${PYTORCH_EXTENSION_SOURCES_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/PytorchNvCodec")
    
endif(GENERATE_PYTORCH_EXTENSION)
