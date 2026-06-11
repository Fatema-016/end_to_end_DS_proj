from setuptools import find_packages, setup

setup(
    name="datascience",
    version="0.0.1",
    author="Fatema",
    description="An end-to-end Data Science MLOps pipeline package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)