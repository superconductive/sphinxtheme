from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name='cakephpsphinx',
    version=__version__,
    author="CakePHP Community",
    author_email="docs@cakephp.org",
    description="CakePHP Sphinx theme and common configuration",
    url="https://book.cakephp.org",
    packages=find_packages(),
    include_package_data=True,
    install_requires='',
    entry_points={}
)
