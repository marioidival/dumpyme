import os
from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.md')) as f:
    README = f.read()

setup(
    name="dumpyme",
    version="0.0.0",
    author="Mario Idival",
    author_email="marioidival@gmail.com",
    description=("Command line package to get dumps"),
    long_description=README,
    license="MIT",
    keywords="dump dumpyme mongo postgres mysql",
    url="https://github.com/marioidival/dumpyme",
    packages=['src'],
    install_requires=[],
    tests_require=['nose', 'coverage'],
    test_suite='tests',
    entry_points='''
        [console_scripts]
        dumpy=src.commander:dumpy
    ''',
    classifiers=[
    ],
)
