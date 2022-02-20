# flake8: noqa
# pylint: skip-file

from os import path
from setuptools import setup, find_packages

__version__ = None
exec(open("borg/version.py").read())

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()
    LONG_DESCRIPTION_TYPE = "text/markdown"

setup(
    name="borg",
    version=__version__,
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    url="",
    download_url="https://github.com/christophsk/borg",
    license="MIT",
    author="C Skiscim",
    author_email="",
    description="borg: Alex Martelli's alternative to the singleton design pattern",
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_TYPE,
    keywords="borg shared-state singleton",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
    ],
)