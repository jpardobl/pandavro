from setuptools import setup
from setuptools import find_packages

setup(
    name='pandavro',
    version='1.2.0',
    description='The interface between Avro and pandas DataFrame(fork from https://github.com/ynqa/pandavro)',
    url='https://github.com/jpardobl/pandavro',
    author='Javier Pardo Blasco',
    author_email='jpard@digitalhigh.es',
    license='MIT',
    packages=find_packages(exclude=['example']),
    install_requires=[
        'fastavro>=0.14.7',
        'numpy',
        'pandas',
    ],
    extras_require={
        'tests': ['pytest'],
    },
)
