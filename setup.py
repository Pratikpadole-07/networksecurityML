from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """Returns a list of requirements from requirements.txt"""
    requirements = []
    try:
        with open("requirements.txt", "r") as f:
            for line in f:
                req = line.strip()
                if req and req != "-e .":
                    requirements.append(req)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements

print(get_requirements())


setup(
    name='NetworkSecurityML',
    version='0.0.1',
    author='Pratik',
    author_email='pratikpadole07@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)