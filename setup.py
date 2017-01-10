# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages
import os
import sys


_version = '0.7.3'
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "pylint-factory is a Pylint plugin to aid Pylint in recognising and understanding" \
                     " errors caused when using the Factory Boy test fixture framework"

_transform_dir = 'pylint_factory/transforms/transforms'
_package_data = {
    'pylint_factory': [
        os.path.join('transforms/transforms', name) for name in os.listdir(_transform_dir)
    ]
}

_classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
)

_install_requires = [
    'pylint>=1.0',
    'pylint-plugin-utils>=0.2.4',
]


setup(
    name='pylint-factory',
    url='https://github.com/singingwolfboy/pylint-factory',
    author='David Baumgold',
    author_email='david@davidbaumgold.com',
    description=_short_description,
    version=_version,
    packages=_packages,
    package_data=_package_data,
    install_requires=_install_requires,
    license='MIT',
    classifiers=_classifiers,
    keywords='pylint factory_boy plugin',
    zip_safe=False,
)
