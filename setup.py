import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="s3jsonl",
    version="0.1",
    author="Adam Szalkowski",
    author_email="adam.szalkowski@tamedia.ch",
    description="Utility functions to read jsonl files from S3 archives",
    long_description=read("Readme.md"),
    license="MIT",
    url="https://github.com/tamediadigital/s3jsonl/",
    packages=["s3jsonl"],
    dependencies=["boto3"],
    tests="tests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
