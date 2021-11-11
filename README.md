# Sustainable Development Goals - Label Classifier

SDG - Label Classifier is a N-Gram based NLP model that can label any given text to its respective Sustainable Development Goals as prescribed by the United Nations. You can read more about it [here](https://sdgs.un.org/goals).

## Live Demo

Two versions of the app has been deployed on the web. One being the REST Server which you could use to call it for your custom applications. The other one being a simple Graphical Web Application that makes calls to the REST APIs an displays the result on the web browser.

### REST Server

* [Server](http://vigneshwarans.pythonanywhere.com/) `vigneshwarans.pythonanywhere.com`
* APIs
    * `/classify` - This api can be used to classify plain text

    ```
    { 
        "text": "TEXT TO CLASSIFY"
    }
    ```
    * `/classifyPDF` - This api can used to classify PDF text. Unlinke the `/classify` api, it takes Multi-part/formdata as input. It only works with PDF and does not support any other format
    ```
    {
        "start": 20,
        "end": 32,
        "file": PDF_BUFFER
    }
    ```

### Web Application

There is nothing much to the Web Application as it is initutive. You can access it [here](https://sdg-classifier.web.app/).

## How it works?

> To be updated


License
----

MIT
