from setuptools import find_packages,setup

from typing import List 

HYPE_E_DOT='-e .'
def  get_requirements(file_path:str)->List[str]:

    '''
        this function return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPE_E_DOT in requirements:
        requirements.remove(HYPE_E_DOT)

    return requirements 

setup(
name='ML-PROJECT',
version='0.0.1',
author='Mehnaz khan',
author_email='mehnazkhan.kpg@gmail.com',
packages=find_packages(),
install_requries=get_requirements('requirements.txt')
)
