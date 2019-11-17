from setuptools import find_packages
from setuptools import setup

setup(
    name='save-the-prince',
    version='0.0.1',
    packages=find_packages(include=('savetheprince*',)),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'dataclasses==0.7',
        'pygame==1.9.6',
    ],
    extras_require={
        'tests': ['mypy==0.740'],
    },
)