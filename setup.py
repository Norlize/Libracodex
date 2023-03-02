from setuptools import setup, find_packages

setup(
    name="LibraCodex",
    version="0.2",
    author="Norlize",
    author_email="norlizyber0@gmail.com",
    description="a simple library fot local files management by collect multiple paths in once times.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["LibraCodex.py"],
    package_data={
        "LibraCodex": [
            "/absolute/path/to/LibraCodex/__init__.py",
            "/absolute/path/to/LibraCodex/main_source.py",
            "/absolute/path/to/LibraCodex/example.py",
            "/absolute/path/to/LibraCodex/README.md",
            "/absolute/path/to/LibraCodex/LICENSE.txt"
        ]
    },
    data_files=[
        ("/absolute/path/to/LibraCodex", ["setup.py"])
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls = {
        "Source code":'https://github.com/Norlize/Libracodex'
    },
)
