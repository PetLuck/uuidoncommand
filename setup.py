# setup.py
from setuptools import setup, find_packages

setup(
    name='uuidoncommand',
    version='0.1.0',
    description='A package used for better UUID generation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Michael Jackson',
    author_email='',
    url='',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
