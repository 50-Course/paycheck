#!/usr/bin/env python3

import os
from setuptools import find_packages, setup


AUTHOR = "Eri A."
PROJECT_DIR = os.path.dirname(__file__)
REQUIREMENTS_DIR = os.path.join(PROJECT_DIR, "requirements")
VERSION = "1.0.0"


def get_requirements(env):
    with open(os.path.join(REQUIREMENTS_DIR, f"{env}.txt")) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


install_requires = get_requirements("base")
setup(
    name="paycheck",
    description="Fintech API for making financial liefs easier for everyone.",
    long_description="A fintech API that provides a simple and easy way to make financial life easier for everyone. "
    "Paycheck allows you to have fast access to loans, build up credit history, make financial transactions at the speed of light "
    "and do some other interesting things.",
    version=VERSION,
    author=AUTHOR,
    author_email="eridotdev@gmail.com",
    find_packages=find_packages("src"),
    install_requires=install_requires,
    package_dir={"": "src"},
    include_package_data=True,
    scripts=paycheck,
)
