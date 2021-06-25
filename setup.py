from setuptools import setup, find_packages
import os
import subprocess


# Required Informations -------------------------------------------------------------------------------------------

PACKAGE_NAME = ""

VERSION_FOLDER_NAME = ""  # The folder name where you want to store your version.py

SHORT_DESCRIPTION = ""  # a short description about package not required cuz you should have all info in README.md file

LONG_DESCRIPTION_FILE_PATH = "README.md"  # this is where you write about your package/project.

URL = ""  # Your source code url like Github

REQUIREMENTS_FILE_PATH = "requirements.txt"  # requirements.txt file

KEYWORDS = []  # This helps to show your package when you search by these keywords.

AUTHOR = ""  # Author/developer's name

# ------------------------------------------------------------------------------------------------------------------


project_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in project_version

assert os.path.isfile(f"{VERSION_FOLDER_NAME}/version.py")

with open(f"{VERSION_FOLDER_NAME}/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{project_version}\n")


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name=PACKAGE_NAME,
    version=project_version,
    author=AUTHOR,
    author_email="",
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description=SHORT_DESCRIPTION,
    packages=find_packages(),
    url=URL,
    package_data={'HTMLTemplateRender': ['VERSION']},
    install_requires=open(REQUIREMENTS_FILE_PATH).read().split("\n"),
    keywords=KEYWORDS,
    classifiers=[
        f"Github :: {URL}",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
