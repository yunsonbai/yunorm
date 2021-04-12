# coding=utf-8
import os
from setuptools import setup


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


setup(
    name="yunorm",
    version="0.4.3",
    packages=get_packages('yunorm'),
    author="yunsonbai",
    author_email='1572120849@qq.com',
    url="https://github.com/yunsonbai/yunorm",
    description="A small ORM but It's very practical",
    long_description="Usage document: https://github.com/yunsonbai/yunorm",
    license="Apache",
    install_requires=["mysqlclient==1.3.14", "mysql-connector-python==8.0.15"],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: Apache Software License",
        'Operating System :: OS Independent',
    ]
)
