# RASA-Spoiler-NLU
A setup to work on the Spoiler detection via RASA  and to store the examples on how to setup

# Requirements
The requirements for the current project are : \
 -> tensorlfow gpu / cpu.\
 -> rasa.\
 -> keras.\
For Rasa installation you can follow this [page](https://chatbotslife.com/set-up-and-get-rasa-nluand-rasa-core-up-and-running-like-a-pro-part-2-b7663b2443c7). It will help in complete installation.\
As for tensorflow, GPU or CPU will work however GPU will be much better in long term for heavier projects. 


# Files and the content
**models** - Contains the saved model for this example. \
\
**policies.yaml** - Contains the training process and what specific entity recognisers are required. For easy understanding refer the image [here](https://blog.rasa.com/rasa-nlu-in-depth-part-2-entity-recognition/).\
\
**spoiler.md** - Contains the training data. It is written in Markdown. This is a basic structure of how to setup intents and lookup tables. You can refer [here](https://rasa.com/docs/rasa/nlu/training-data-format/) for better understanding and examples. \
\
**test_spoilers.py** - Contains the simple testing script for the model.\
\
**tester.ipynb** - Contains a notebook version of the test_spoiler.py with explanation line by line. \
\
**trainer.ipynb** -Contains a notebook verion of the trainer.py with explanation line by line.
