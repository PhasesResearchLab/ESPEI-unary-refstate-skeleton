# Skeleton for providing reference states as plugins for ESPEI

## How to use this repository

Installing this repository 

* Clone it locally (`git clone https://PhasesResearchLab/ESPEI-refstate-skeleton`)
* Install it using `pip` (`cd ESPEI-refstate-skeleton` and then `pip install -e .`)
* 

## How to modify this repository

* Clone it locally (`git clone https://PhasesResearchLab/ESPEI-refstate-skeleton`)
* Open the `setup.py` file and change the `NAME` variable at the top to your desired name. I suggest something like `espei_refstate_<name>`, for example `espei_refstate_bock2015` if your reference state will be called `BOCK2015`
* Add two dictionaries to the `refstate.py` module named `BOCK2015` and `BOCK2015Stable`, corresponding to the energy of the SER reference phase at 298.15 K and the lattice stabilities, respectively, as SymPy expressions. The best way to do this is just look at what's there and modify the example.

## Background

Packages provide plugins by using the `entry_points` feature of the Python package `setuptools`.

Some helpful links are:

* (most introductory) [using package metadata entry_points](https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata)
* [entry_points specification](https://packaging.python.org/specifications/entry-points/)
* [how setuptools finds plugins](https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins)

