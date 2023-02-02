import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='gitlatexdiff',  
     version='0.0.1',
     scripts=['gitlatexdiff'] ,
     author="Géry Casiez",
     author_email="gery.casiez@gmail.com",
     description="Allows to create a document that highlights the diff between two git versions of a LaTeX document.",
     long_description=long_description,

     long_description_content_type="text/markdown",
     url="https://github.com/casiez/gitlatexdiff",
     packages=setuptools.find_packages(),
     install_requires=[ 'argparse'],

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: MacOS",
     ],

 )