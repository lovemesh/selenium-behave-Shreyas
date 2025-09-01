from setuptools import setup, find_packages

setup(
    name="selenium-behave",
    version="0.1.0",
    description="A Behave + Selenium Page Object Model framework with auto-generated structure and predefined steps",
    author="Shreyas Patil",
    author_email="shreyas71190@gmail.com",
    url="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "selenium>=4.0.0",
        "behave>=1.2.6"
    ],
    entry_points={
        "console_scripts": [
            "selenium-behave-gen=selenium_behave.cli:main",  # lets you run: selenium-behave gen
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Behave",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)

