from setuptools import setup, find_packages

setup(
    name="revlibs-dicts",
    version="0.0.1",
    author="Demeter Sztanko",
    author_email="demeter.sztanko@revolut.com",
    py_modules=["revlibs.dicts"],
    python_requires=">=3.6",
    install_requires=["ruamel.yaml>=0.15.89"],
    namescape_packages=["revlibs"],
)
