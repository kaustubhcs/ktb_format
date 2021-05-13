from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Python and C++ ASCII to Binary Packer and Unpacker'
LONG_DESCRIPTION = 'Packages ASCII data to Binary using KTB (Keep That Bit) format.'

setup(
    name="ktb_format",
    version=VERSION,
    author="Kaustubh Shivdikar",
    author_email="kaustubhcs07@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['ktb_format', 'binary', 'pack', 'unpack', 'ktb'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ]
)
