import setuptools
import sys
from typing import List
from src.Renel_Disease_Classifier.exception import RenelException
from src.Renel_Disease_Classifier.logger import logging


def get_requirements() -> List[str]:
    requirements_list: List[str] = []

    try:
        # logging.info("trying to open requirementrs.txt file")
        with open("requirements.txt", "r") as f:
            requirements_list = f.readlines()

    except Exception as e:
        # logging.exception(f"an error occcured {e}")
        # raise RenelException(e, sys)
        raise e

    # Strip newline characters and remove '-e .' from the list
    requirements_list = [
        requirement.strip()
        for requirement in requirements_list
        if requirement.strip() != "-e ."
    ]

    return requirements_list


__version__ = "0.0.1"

REPO_NAME = "Renel_Disease_Classification_Deep_Learning "
AUTHOR_USER_NAME = "Jatindra Paul"
SRC_REPO = "Renel_Disease_Classifier"
AUTHOR_EMAIL = "jatindrapaul7@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description_content="text/markdown",
    url="https://github.com/Jatindra23/Renel_Disease_Classification_Deep_Learning",
    project_urls={
        "Bug Tracker": "https://github.com/jatindrapaul7/Renel_Disease_Classification_Deep_Learning/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements(),
)
