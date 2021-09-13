from os import chdir
from os.path import abspath, dirname, join, normpath
from setuptools import find_packages, setup

with open(join(dirname(__file__), "README.md")) as readme:
    README = readme.read()


# allow setup.py to be run from any path
chdir(normpath(abspath(dirname(__file__))))

import simple_svg  # noqa

setup(
    name="django-simple-svg",
    version=simple_svg.__version__,
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    license=simple_svg.__license__,
    description=simple_svg.__doc__,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/xshapira/django-simple-svg",
    author="Max Shapira",
    author_email="max@winoutt.com",
    maintainer="Max Shapira",
    maintainer_email="max@winoutt.com",
    install_requires=["Django>=1.8"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    test_suite="tests",
)
