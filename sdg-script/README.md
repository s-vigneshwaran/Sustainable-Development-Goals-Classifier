# Sustainable Development Goals - Script

## Installation

Install the dependencies 

```sh
$ pip3 install -r requirements.txt
```

## Usage
```sh
$ python3 application.py INPUT.csv INDIVIDUAL_FLAG FOS_FLAG
```

`INPUT.csv`
```
name,location,start,end
```

> Location can be either absolute or relative path to the current working directory

`INDIVIDUAL_FLAG` If set to 1, then a csv file is produced corresponding to every input pdf. Anything else, produces a single output.

`FOS_FLAG` If set to 1, then additional output file with the details of the field of study is generated. Anything else does nothing.

### Examples
```sh
$ python3 application.py 0 0
```
> Produces single output file

```sh
$ python3 application.py 1 0
```
> Produces multiple output files

```sh
$ python3 application.py 0 1
```
> Produces single output file along with another fos file
```sh
$ python3 application.py 1 1
```
> Produces multiple output files along with multiple fos files


## Tech

Sustainable Development Goal - Script uses a number of open source projects to work properly:

* numpy - NumPy is the fundamental package for array computing with Python.
* pandas - Powerful data structures for data analysis, time series, and statistics
* PyPDF2 - A Pure-Python library built as a PDF toolkit
* typing - Type Hints for Python


## How it works?

SDG-Script uses the same computational logic as the python notebook in the root directory. Refer to the notebook for indepth explanation.


License
----

MIT
