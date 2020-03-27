# Skeleton for providing reference states as plugins for ESPEI

## How to use this repository

Installing this repository:

* Clone it locally (`git clone https://PhasesResearchLab/ESPEI-unary-refstate-skeleton`)
* Install it using `pip` (adding the `-e` flag to make it editable, i.e. you change change the reference state data and it will take effect) (`cd ESPEI-unary-refstate-skeleton` and then `pip install -e .`)

Once you have done this, you'll be able to use the reference state defined by the `NAME` variable in `setup.py`, which defaults to `CustomRefstate2020` in ESPEI for parameter generation, i.e. in the following input YAML:

```yaml
system:
  phase_models: my-phases.json
  datasets: my-input-datasets
generate_parameters:
  excess_model: linear
  ref_state: CustomRefstate2020
```

See below for how to modify this to use your own reference state!

## How to modify this repository

* Clone it locally (`git clone https://PhasesResearchLab/ESPEI-unary-refstate-skeleton`) and enter the package directory (`cd ESPEI-unary-refstate-skeleton`). You can rename the directory if you like.
* Open the `setup.py` file and change the `NAME` variable at the top of the file to your desired name. I suggest something like `Bocklund2015`. This must correspond to the names of the dictionaries in the next step.
* Add two dictionaries to the `refstate.py` module named `<NAME>Stable` and `<NAME>` (e.g. `Bocklund2015` and `Bocklund2015`), corresponding to the energy of the stable phase at 298.15 K and the lattice stabilities, respectively, as SymPy expressions. The best way to do this is just look at what's there and modify the example. *Note that the names are case sensitive and they must be valid Python identifiers!* Python identifiers start with a letter and contain only letters, numbers and underscores.
* Install the package as editable 

## Background

Packages provide plugins by using the `entry_points` feature of the Python package `setuptools`.

Some helpful links are:

* (most introductory) [using package metadata entry_points](https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata)
* [entry_points specification](https://packaging.python.org/specifications/entry-points/)
* [how setuptools finds plugins](https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins)

## Debugging

If you want to test whether your modules are found, you can run the following Python code to show what reference states were found 

```python
import espei
print(espei.refdata.INSERTED_USER_REFERENCE_STATES)
```

If you do this after installing the unchanged package from this repository, you should find `CustomRefstate2020` is printed and the dictionaries `espei.refdata.CustomRefstate2020Stable` and `espei.refdata.CustomRefstate2020` should be defined.

For more details see the `espei.refdata.find_and_insert_user_refstate` function.
