"""Python setup.py for mot_con package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("mot_con", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="mot_con",
    version=read("mot_con", "VERSION"),
    description="Awesome mot_con created by BhatAjaz",
    url="https://github.com/BhatAjaz/mot_con/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="BhatAjaz",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["mot_con = mot_con.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
