from setuptools import setup, find_packages
from os import path


PWD = path.abspath(path.dirname(__file__))

with open(path.join(PWD, 'README.md')) as fp:
    long_description = fp.read()

install_requires = [
]

setup(
    name = 'uptime-robot',
    verion = '0.0.0',
    description = 'Check your server regularly.',
    long_description = long_description,
    url = 'https://github.com/channprj/uptime-robot',
    author = 'CHANN',
    author_email = 'chann@chann.kr',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: CLI, Web',
        'Topic :: Server',
        'Topic :: Internet',
    ],
    keywords = 'uptime monitor',
    packages = find_packages(),
    install_requires = install_requires,
)
