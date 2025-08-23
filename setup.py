# This setup.py will be responsible in creating my machine learning application
# as a package.We can install this package in our project and can use it 
# This would allow us to build our entire machine learning application as
# a package and even deploy pipeline


from setuptools import find_packages,setup #Find all the packages
# in the ML learning application

# This is metadata info about the entire project

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    # This function will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Tridib',
    author_email='tridibroychowdhury9@gmail.com',
    packages=find_packages(),
    # It checks in how many packages do we have this __init__.py 
    # So it would directly consider this source as a package itself
    # and it would try to build it
    install_requires=get_requirements('requirements.txt')


)

# We can directly install this setup.py or 
# while install all the packages in requirements.txt this setup.py
# should also run ro build the packages

# -e .-->This automatically triggers setup.py

