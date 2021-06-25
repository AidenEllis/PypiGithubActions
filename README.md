## PypiGithubActions

* This is a boilerplate for uploading Python package from GitHub using GitHub's Actions automation.
* This guide will show you the easiest and secure way to do publish you packages using GitHub


### Creating and Uploading Python Package
<hr>

### 💫 Naming the package :

<b>

It's crucial that your package name is unique, it means that
there shouldn't be any other packages in Pypi named the same 
package name you want.

Yeah, but how are we going to know that our package name is unique?

For that open your web browser and type https://pypi.org/project/YOUR_PACKAGE_NAME
If it shows the package that means there's already a package named as it.
If there's no package named as that, it will show you a 404 page, Which means
there's no package named to that, so you can use it.

</b>

###

### ⚡️ Creating a git repository :
<b>

Now let's create a git repository, NOTE: the git repository should be the same name as
your package name, (Repository can be public or private).

Now inside that repository you need to have a python folder (where you have `__init__.py` in the folder)
NOTE: this folder also needs to be the same name as the package name, so both the
repository and Package folder needs to be the same name as the package name

now you can go on and build your package inside that python folder.

</b>

###

### 🌈 Setting up Required stuffs for the package :

<b>

Inside that python package folder create a file named `version.py` and paste this
chunk of code in that version.py file

```python
import os


def string():
    try:
        with open(os.path.dirname(__file__) + "/VERSION", "r", encoding="utf-8") as fh:
            version = fh.read().strip()
            if version:
                return version
    except:
        pass
    return "unknown (git checkout)"
```

This will help on automatically deceting the package version.

INFO: You can also find this code in this repository `version.py`

Now in the project root folder (outside your python package folder) create a file
name `setup.py` This file is really important because this file contains all the information
about your package.After creating this paste this code inside it


```python
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

```

Again, this code is available in this repository (`setup.py`)

Open that file and Fill in the required information:

</b>

`PACKAGE_NAME` : Name of your package

`VERSION_FOLDER_NAME`: This is also your package name, this is the folder name
where you store that version.py file.

`SHORT_DESCRIPTION` : short description about your Package (This is not required)

`LONG_DESCRIPTION_FILE_PATH` : this is the long description path like README.md this will be in the root folder aso you don't need to change it unless you've stored it somewhere else.

`URL` : Source code url: Your GitHub Repository URL that you just created for the package.

`REQUIREMENTS_FILE_PATH` : requirements.py file, this also need to be at the root folder of your project so, no need to change.

`KEYWORDS`: Keywords for searching your package in pypi website

`AUTHOR`: Author/Developer name, it's You.

###
### 🌙 Setting GitHub workflow :

<b>

We are really close to it! in the root folder create a new folder named `.github`
and inside it create another folder named `workflows` inside it create a new file 
named pypi.yml (You can name it anything with a .yml extention) inside it paste this code:

```yaml
name: Upload Python Package

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-20.04

    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v2
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel twine
    - name: Build and publish
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN  }}
      run: |
        python setup.py sdist bdist_wheel
        twine upload dist/*
```

You can get this code in this repository.

🥳 Congratulations! That's all we need! It's time to go and push it to GitHub
Now go on and push it to Your GitHub Repository

</b>

###
### ☄️ Uploading our package :

<b>

In your repostory got to `settings` then in the left menu find
`secrets`, click on it, then on the right side you will see 
`NEW REPOSITORY SECRET` button, click it and set the Name to : `PYPI_API_TOKEN`
and enter Your pypi api key and click add secret.

If you don't know how to get pypi api key:

Go to https://pypi.org then Login or Register then after you're
logged in click in the right corner where it shows your name then click
`Account settings` now scroll down until you see the create api section
then create the api.


🥵 Finally it's time to upload our package.

go to your GitHub package repository, on the right side click
`Releases` then click `draft a new release` then enter the version
number you want, you can start with `1.0.0` in the title Enter your
package name with the version like `PackageName 1.0.0`

Now click `Publish Release`

Now in the top menu go to `Actions` then you will see a workflow running
click it and then click deploy, after process is done if it shows success then
Voilà! 🥳🥳🥳🥳🥳 Your Mission is done.

I'm so tired now, imma go get some sleep and cuddle my cat :3 happy meow meow
🐱

</b>




