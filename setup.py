from os import name
from sys import version
from setuptools import setup


with open("README.md","r",encoding='utf-8') as f:
    long_description=f.read()


setup(
    name="src",
    version="0.0.1",
    author="gaurav98094",
    description="Simple ANN Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaurav98094/ANN-Implementation",
    author_email="kandelgaurav7@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)