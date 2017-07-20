#!/usr/bin/env python
from setuptools import setup

desc = """timecourse-sample-recorder: record exact sampling times"""

install_requires = [
]

test_requires = [
]

pypi_classifiers = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

setup(
    name="timecourse-sample-recorder",
    py_modules=["sampler"],
    version="0.0.1",
    install_requires=install_requires,
    tests_require=test_requires,
    description=desc,
    author="Kevin Murray",
    author_email="kdmfoss@gmail.com",
    url="https://github.com/kdmurray91/timecourse-sample-recorder",
    keywords=["timecourse"],
    classifiers=pypi_classifiers,
    entry_points={
        'console_scripts': [
            'timecourse-sample-recorder=sampler:main',
        ],
    },
)
