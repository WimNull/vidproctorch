from setuptools import setup, find_packages

packages_name = 'PyNvCodec'

setup(
    name=packages_name,
    version="0.2.0",
    description="Using gpu decode video.",
    author="wimnull",
    classifiers=[
        "Development Status :: 4 - Beta", "Environment :: GPU :: NVIDIA CUDA",
        "License :: OSI Approved :: BSD License", "Intended Audience :: Developers",
        "Intended Audience :: Science/Research", "Operating System :: POSIX :: Linux", "Programming Language :: C++",
        "Programming Language :: Python", "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering", "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development", "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.6',
    packages=[packages_name],
    package_data={'':["*.pyi", '*.py', '*.so']},
)
