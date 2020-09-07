import codecs
import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Terminal Todo',
    version='0.0.1',
    description='command-line todo tools to keeping the track of your tasks',
    long_description=long_description,
    keywords='todo list task management track',
    author='Sullivan Z',
    author_email='salar.z@outlook.de',
    url='https://github.com/Epic-R-R/tTodo',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'todo=todo:main'
        ]
    }
)
