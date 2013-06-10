# coding: utf-8

from __future__ import with_statement
from setuptools import setup


def get_version(fname='nose_faulthandler.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='nose-faulthandler',
    version=get_version(),
    description='Nose plugin. Activates faulthandler module for test runs.',
    long_description=get_long_description(),
    keywords='nose testing',
    author='Marc Schlaich',
    author_email='marc.schlaich@gmail.com',
    url='https://github.com/schlamar/nose-faulthandler',
    license='MIT',
    py_modules=['nose_faulthandler'],
    zip_safe=False,
    install_requires=['faulthandler'],
    entry_points={
        'nose.plugins': [
            'nose_faulthandler = nose_faulthandler:FaultHandler',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
