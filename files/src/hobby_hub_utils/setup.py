import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hobby-hub-pkg", 
    version="0.0.4",
    author="Rock, Draven, Anthony, Declan, Andy",
    author_email="schillingdl@msoe.edu",
    description="Hobby Hub utility package. Developed for BeagleBone Green",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Senior-Design-0x07/the-hobby-hub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
