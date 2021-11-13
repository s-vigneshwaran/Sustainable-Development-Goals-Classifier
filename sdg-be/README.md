# Sustainable Development Goals - Back End

## Installation

Install the dependencies 

```sh
$ pip3 install -r requirements.txt
```
### To run the developmental server
```sh
$ python3 application.py
```

## Tech

Sustainable Development Goal - BE uses a number of open source projects to work properly:

* numpy - NumPy is the fundamental package for array computing with Python.
* PyPDF2 - A Pure-Python library built as a PDF toolkit
* typing - Type Hints for Python
* flask - A simple framework for building complex web applications
* flask-cors - A Flask extension adding a decorator for CORS support

# APIs
* `/classify` - This api can be used to classify plain text

```
{ 
    "text": "TEXT TO CLASSIFY"
}
```
* `/classifyPDF` - This api can used to classify PDF text. Unlinke the `/classify` api, it takes Multi-part/formdata as input. It only works with PDF and does not support any other format. `start` and `end` refers to the page range.
```
{
    "start": 20,
    "end": 32,
    "file": PDF_BUFFER
}
```

## How it works?

SDG-BE uses the same computational logic as the python notebook in the root directory. Refer to the notebook for indepth explanation.

> Live demo available at : `sdg-classifier.web.app`


License
----

MIT
