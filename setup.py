#This is responsible for creating my machine learning application as a package
from setuptools import find_packages,setup  #this is importing two important functions from the setuptools package,which is widely used for packaginf and distrubuting python project
from typing import List

HYPEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    
    name='mlproject',  # Replace with the name of your project
    version='0.0.1',  # Initial version of your project
    packages=find_packages(),  # Automatically finds and lists all packages
    install_requires=get_requirements('requirements.txt'),
    author='Bishmay',  # Your name or the author's name
    author_email='bishmay.padhi@gmail.com',  # Your email
    
)
