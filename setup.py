import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()
    

__version__ = "0.0.0"

REPO_NAME="ReySilico"
AUTHOR_USER_NAME="Vishal_Nagar"
SRC_REPO="ReySilico"
AUTHOR_EMAIL="vishalnagar410@gmail.com"

setuptools.setup(
    name=SCR_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "A python package for QSAR and molecular Docking",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=stuptools.find_packages(where="src")
    
)