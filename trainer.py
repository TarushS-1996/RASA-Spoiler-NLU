import rasa.nlu
import rasa.core
import spacy

from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer, Interpreter 
from rasa.nlu import config 

import random

train_data = load_data("spoiler.md")
trainer = Trainer(config.load("policies.yaml"))
interpreter = trainer.train(train_data)
model_direct = trainer.persist("./models/nlu", fixed_model_name = "spoiler_detection")

print("Model training done !!!!!!!!!")
