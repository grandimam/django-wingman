from setuptools import setup, find_packages

setup(
    name='core',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'django>=3.2',
    ],
    description='A Django library for Feature Flag functionality.',
    author='Fauzan',
    license='MIT',
    url='https://github.com/grandimam/wingman',
)
