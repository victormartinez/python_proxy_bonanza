# -*- coding: utf-8 -*-
import os
from codecs import open
from os.path import abspath, dirname, join

from pip.req import parse_requirements
from setuptools import setup, find_packages

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


def _to_list(requires):
    return [str(ir.req) for ir in requires]


def _get_version():
    path_to_init = os.path.join(os.path.dirname(__file__), 'proxy_bonanza', '__init__.py')
    version_line = list(filter(lambda l: l.startswith('VERSION'), open(path_to_init)))[0]
    version_tuple = eval(version_line.split('=')[-1])
    return '.'.join(map(str, version_tuple))


install_requires = _to_list(parse_requirements('requirements.txt', session=False))
tests_require = _to_list(parse_requirements('requirements-test.txt', session=False))
VERSION = _get_version()

setup(
    name='proxy_bonanza',
    version=VERSION,
    description='A lightweight python client for Proxy Bonanza service',
    long_description=long_description,
    url='http://github.com/victormartinez/python_proxy_bonanza',
    license='MIT License',
    author='Victor Martinez',
    author_email='vcrmartinez@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['proxy', 'bonanza'],
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=['pytest-runner==2.8']
)
