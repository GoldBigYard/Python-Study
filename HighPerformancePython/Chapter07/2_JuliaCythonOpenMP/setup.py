# Example 7-11
from distutils.core import setup
from distutils.extension import Extension

import numpy
from Cython.Build import cythonize

ext_modules = [
    Extension("cythonfn", ["cythonfn.pyx"], extra_compile_args=['-fopenmp'], extra_link_args=['-fopenmp'])
]

setup(ext_modules=cythonize(ext_modules, compiler_directives={"language_level": "3"}), include_dirs=[numpy.get_include()])
