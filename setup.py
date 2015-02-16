import os
from setuptools import setup, find_packages

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.rst')) as f:
    README = f.read()

setup(
    name="dumpyme",
    version="0.1.0",
    author="Mario Idival",
    author_email="marioidival@gmail.com",
    description=("Command line package to get dump databases"),
    long_description=README,
    license="MIT",
    keywords="dump dumpyme mongodb postgres mysql databases",
    url="https://github.com/marioidival/dumpyme",
    packages=find_packages(),
    install_requires=['click', 'fabric'],
    tests_require=['nose', 'coverage'],
    test_suite='tests',
    package_data = {
        '': ['*.ini'],
    },
    entry_points='''
        [console_scripts]
        dumpy=src.commander:dumpy
    ''',
    classifiers=[
    ],
)
