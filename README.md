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
    * `/classifyPDF` - This api can used to classify PDF text. Unlinke the `/classify` api, it takes Multi-part/formdata as input. It only works with PDF and does not support any other format. `start` and `end` refers to the page range.
    ```
    {
        "start": 20,
        "end": 32,
        "file": PDF_BUFFER
    }
    ```

### Web Application

There is nothing much to the Web Application as it is initutive. You can access it [here](https://sdg-classifier.web.app/). `sdg-classifier.web.app`

## Local Machine Script

In order to facilitate processing of multiple PDFs at once, you could leverage the functionalities of the `sdg-script` tool. For more details, open the sub-directory and read the README.md


# How it works?

* Given a text, the application extracts all possible grams(set by implementer) of words from it.
* Each and every gram is iterated on the existing Fields Of Study and if it exists the ids of the field of study and its frequency is noted
* Now that we have the Fields of Study and Frequencies, we can start mapping the respective Sustainable Development Goal. The mapping is done with respect to the existing data as well.
* All the frequencies of the SDG is added and the sum is the relevancy score of that particular SDG.

> For the implementaion details, take a look at the notebook

## Data Availabilty and Reference

The data is taken from the OSDG.ai's [osdg-tool](https://github.com/osdg-ai/osdg-tool/tree/main) repository. The idea of using a NGram based approach is also taken from the project.

License
----

MIT
