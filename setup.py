import codecs
import os

from setuptools import setup, find_packages
long_description = 'A simple command-line todo tools to keeping the track of your tasks Built with Python 3 with Linux systems.' \
                   'tTodo does not have a graphical interface have a graphic interface' \

setup(
    name='tTodo',
    version='0.1',
    description='command-line todo tools to keeping the track of your tasks',
    long_description=long_description,
    author='Sullivan Z',
    author_email='salar.z@outlook.de',
    url='https://github.com/Epic-R-R/tTodo',
    keywords=['todo', 'list', 'task', 'management', 'manager', 'track'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
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
