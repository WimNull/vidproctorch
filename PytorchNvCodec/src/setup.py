from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

pkname = 'LibPytorchNvCodec'
setup(name=pkname,
    ext_modules=[CUDAExtension(pkname, ['PytorchNvCodec.cpp'])],
    cmdclass={
        'build_ext': BuildExtension
    })