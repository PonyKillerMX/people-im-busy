import setuptools 

with open("README.md", "r") as fh: 
    long_description = fh.read() 

setuptools.setup(
    name="people-im-busy", 
    version="0.1", 
    scripts=["people-im-busy.py"], 
    author="Emilio Andere", 
    author_email="emilioanderevalencia@gmail.com",
    descriptioin="A package to message people saying you're busy", 
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url="https://github.com/PonyKillerMX/people-im-busy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language: :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System:: OS Independent",
    ],
)
