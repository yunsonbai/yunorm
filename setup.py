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
    version="0.3.0",
    packages=get_packages('yunorm'),
    author="yunsonbai",
    author_email='1942893504@qq.com',
    url="http://www.yunsonbai.top",
    description='Tool integration:db data statistics/diagram/email',
    install_requires=["mysqlclient==1.3.14"],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
