import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mask-gpu",
    version="0.0.1",
    description="A simple tool to show specified number of GPUs with desired memory to Tensorflow",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/saravanabalagi/mask-gpu",
    author="Saravanabalagi Ramachandran",
    author_email="saravanabalagi@hotmail.com",
    license="MIT",
    classifiers=[
    	"Development Status :: 3 - Alpha",
    	"Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points = {
        'console_scripts': ['mask-gpu=mask_gpu.command_line:main'],
    },
    packages=["mask_gpu"],
    include_package_data=True,
)
