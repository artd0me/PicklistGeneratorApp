from setuptools import setup, find_packages

setup(
    name='picklistgenerator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'datetime',
        'platform'
    ],
    author='Dominik Böhm',
    author_email='d-boehm1@web.de',
    description='Generates ECHO picklists for multicolor stainings',
    url='https://github.com/artd0me/PicklistGeneratorApp',
)