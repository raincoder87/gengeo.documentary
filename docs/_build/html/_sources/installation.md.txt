# Installation

genGEO package is a python-based package which is hosted in [pypi](https://pypi.org/). genGEO can be installed using the following line:

## Automatic Installation
Using the ```pip`` installation program, you can install the official release from the pypi server using:


```console
(.venv) $ pip install gengeo
```

## Manual installation

genGEO uses [conda](https://docs.conda.io/projects/conda/en/latest/index.html) for easy package management and comes with an yml file to create an environment with all required packages.

For conda users please run the following for installation:
- `conda env create -f genGEO.yml`

and for updates:
- `conda env update -f genGEO.yml`



For non conda users, please install the following packages:
- python=3.7 (or higher)
- pandas
- scipy
- coolprop
- xlrd=1.2.0


## Testing

To test if genGEO works fine on your system, please run the tests with the following command:

`cd <path_to_genGEO> ; ./runTests.sh`

For the full test which also tests the optimization mode please run:

`cd <path_to_genGEO> ; ./runTests.sh full`


Contact
---
For contact please visit: [https://geg.ethz.ch/people/](https://geg.ethz.ch/people/)
