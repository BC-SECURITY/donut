from setuptools import Extension, setup
import sys
import platform

with open("README.md", "r") as fh:
    long_description = fh.read()

static_libraries   = []
static_lib_dir     = 'lib'
libraries          = []
library_dirs       = ['lib']
extra_compile_args = []
extra_link_args    = []
extra_objects      = []
include_dirs       = ['include']
sources            = ['donut.c', 
                      'hash.c', 
                      'encrypt.c', 
                      'format.c', 
                      'loader/clib.c', 
                      'donutmodule.c']

if sys.platform == 'darwin' or sys.platform.startswith('linux'):
    arch = platform.machine()
    if arch == 'x86_64':
        extra_compile_args += ["-D", "MAX_PATH=260"]
    elif arch == 'arm64':
        extra_compile_args += ["-D", "MAX_PATH=260"]
elif sys.platform == 'win32':
    library_dirs.append(static_lib_dir)
    extra_objects = []
elif sys.platform == 'win64':
    library_dirs.append(static_lib_dir)
    extra_objects = []
    extra_objects = []



module = Extension(
        "donut",
        include_dirs       = include_dirs,
        sources            = sources,
        libraries          = libraries,
        library_dirs       = library_dirs,
        extra_compile_args = extra_compile_args,
        extra_link_args    = extra_link_args,
        extra_objects      = extra_objects,
)

setup(
     name='donut-shellcode',
     version='1.0.4',
     description='Donut shellcode Python C extension',
     long_description=long_description,
     long_description_content_type="text/markdown",
     license="BSD-3",
     author_email="therealwover@protonmail.com",
     url='https://github.com/TheWover/donut',
     author='TheWover, Odzhan, byt3bl33d3r',
     include_package_data=True,
     zip_safe=True,
     ext_modules=[module],
     python_requires='>=3.0',
)
