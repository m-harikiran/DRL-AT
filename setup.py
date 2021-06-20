from setuptools import setup, find_packages

setup(
    name='DRL-AT',
    version='1.0',
    author='Harikiran M',
    authour_email='harikiran.m@ou.edu',
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
