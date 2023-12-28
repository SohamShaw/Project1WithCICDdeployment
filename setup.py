from setuptools import find_packages,setup
from typing import List

edot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of req
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if edot in requirements:
            requirements.remove(edot)

    return requirements
         
setup(
    name='mlproject',
    version='0.0.1',
    author='Soham',
    author_email='some.one12.m2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')

)