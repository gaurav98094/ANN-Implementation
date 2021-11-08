import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

USER_NAME='gaurav98094'

setuptools.setup(
    name="src",
    version="0.0.3",
    author=f"{USER_NAME}",
    author_email="kandelgaurav7@gmail.com",
    description="ANN Implementation Using KERAS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaurav98094/ANN-Implementation",
    project_urls={
        "Bug Tracker": "https://github.com/gaurav98094/ANN-Implementation/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
    
)