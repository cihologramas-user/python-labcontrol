#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup

setup(
    name='labcontrol',
    version='0.1dev',
    author='Ivan Pulido',
    author_email='ijpulidos@cihologramas.com',
    packages=['thorlabs',],
    #scripts=['exposure/focus.py','exposure/print_c.py', 'exposure/expo_c.py','lib/rebootCamera','exposure/testing_blue_red.py', 'exposure/park.py', 'exposure/scanplate.py', 'exposure/testingAnglesPixsize.py'],
    url='http://www.cihologramas.com',
    description='Control library for lab equipment',
    #ext_modules=cythonize(extensions),
    cmdclass={'build_ext': build_ext},
    long_description=open('README.md').read(),
    #data_files=[("share/firefly", ["lib/rvt.dat"])]
)
