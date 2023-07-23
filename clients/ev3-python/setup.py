# coding: utf-8

"""
    EV3 API

    Welcome to the EV3 API Reference documentation. This API reference provides comprehensive information about status of all EV3 components and resources. <br> Choose Latest spec from dropdown to view API reference on latest version available.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from setuptools import setup, find_packages  # noqa: H301
import os

NAME = "ev3api"
is_tag = os.environ.get("GITHUB_REF_TYPE") == "tag"
VERSION = os.environ.get("GITHUB_REF_NAME") if is_tag else "0.0.0-dev"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "ev3api"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum",
]

setup(
    name=NAME,
    version=VERSION,
    description="EV3 API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/EV3-OpenAPI/EV3-API",
    keywords=["OpenAPI", "OpenAPI-Generator", "EV3 API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="",
    long_description_content_type="text/markdown",
    long_description="""\
    """,
    package_data={"ev3api": ["py.typed"]},
)
