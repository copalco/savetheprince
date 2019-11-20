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
        'pygame==2.0.0.dev6',
    ],
    extras_require={
        'tests': [
            'mypy==0.740',
            'flake8==3.7.9',
            'coverage==4.5.4',
        ],
    },
)
