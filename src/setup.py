from setuptools import find_packages
from setuptools import setup

setup(
    name='save-the-prince',
    version='0.0.1',
    packages=find_packages(include=('savetheprince*',)),
    include_package_data=True,
    zip_safe=False,
)