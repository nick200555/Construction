from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='construction',
    version='1.0.0',
    description='Comprehensive Construction Management System for ERPNext',
    author='Construction Team',
    author_email='admin@construction.org',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
