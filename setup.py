from setuptools import setup, find_packages

with open("README.md") as file:
    long_description = file.read()

setup(
    name="dockubeadt",
    description="Translate Docker compose and k8s manifests to a MiCADO ADT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.2.0",
    author="Resmi Arjun / Jay DesLauriers",
    url="https://github.com/UoW-CPC/DocKubeADT",
    project_urls={
        "Bug Tracker": "https://github.com/UoW-CPC/DocKubeADT/issues",
    },
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=["ruamel.yaml", "click"],

    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["dockubeadt=dockubeadt.cli:main"],
    },
)
