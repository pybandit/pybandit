from setuptools import find_packages, setup


# Function to read the list of requirements from requirements.txt
def read_requirements():
    with open("requirements.txt") as req:
        return req.read().splitlines()


setup(
    name="pybandit",
    version="0.0.1",
    description="Implementation of popular Multiarmed Bandit Algorithms",
    authors=["Tuhin Sharma <tuhinsharma121@gmail.com>"],
    packages=find_packages(),
    install_requires=read_requirements(),
)
