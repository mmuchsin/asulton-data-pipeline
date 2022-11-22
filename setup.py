from setuptools import setup, find_packages
from typing import List

# Setup functions variables
PROJECT_NAME = "asulton-data-pipeline"
VERSION = "1.0"
AUTHOR = "M Muchsin"
DESRCIPTION = "This is a data pipeline for asulton project"
REQUIREMENT_FILE_NAME = "requirements.txt"
EDITABLE = "-e ."


def get_requirements_list() -> List[str]:
    """This function returns a list of requirements
    mention in requirements.txt file without "-e ."

    Returns:
        List[str]: a list of requirements
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [
            requirement_name.replace("\n", "") for requirement_name in requirement_list
        ]
        if EDITABLE in requirement_list:
            requirement_list.remove(EDITABLE)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list(),
)
