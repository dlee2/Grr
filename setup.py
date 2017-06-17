from __future__ import absolute_import

import os

from setuptools import find_packages, setup


def read(filename):
    return open(os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        filename,
    )).read()

third_party_dependencies = (
    "flask",
    "flask_graphql",
    "graphene",
    "graphene_sqlalchemy",
    "sqlalchemy",
)

tests_require = (
    "nose",
)

setup(
    name="Grr Backend",
    version="0.1.0",
    description="Fun with dan and richard",
    long_description=read("README.md"),
    packages=find_packages(exclude=["ez_setup"]),
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    install_requires=third_party_dependencies,
    tests_require=tests_require,
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python",
    ],
    entry_points="""
        [console_scripts]
        flask=flask.cli:main
    """,
)
