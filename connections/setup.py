from setuptools import setup, find_packages

setup(
    name="revlibs-connections",
    version="0.0.1",
    author="Demeter Sztanko",
    author_email="demeter.sztanko@revolut.com",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "revlibs-dicts>=0.0.1",
        "revlibs-logger>=0.0.2",
        "psycopg2>=2.7.7",
        "pyexasol>=0.5.2",
    ],
    namescape_packages=["revlibs"],
)
