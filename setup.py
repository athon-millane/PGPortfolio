from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open('requirements.txt') as f:
    deps = f.read().splitlines()

setup(
    name="pgportfolio",
    version="1.0.0",
    install_requires=deps,
    long_description=readme,
    author="Zhengyao Jiang, Dixing Xu, Jinjun Liang",
    packages=find_packages(),
)