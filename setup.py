from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="myhelloworld",
    version="0.0.1",
    description="Say hello!",
    py_modules=["myhelloworld"],
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],

    install_requires=[
    ],

    extras_require = {
        "dev": [
            "pytest >= 3.7",
        ],
    },
)
