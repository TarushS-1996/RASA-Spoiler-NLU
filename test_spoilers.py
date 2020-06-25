import rasa.nlu
import rasa.core
import spacy

from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer, Interpreter 
from rasa.nlu import config 
from termcolor import colored

interpreter = Interpreter.load("./models/nlu/spoiler_detection")

while True:
	inp = input("Enter query here ::")
	interpret = interpreter.parse(inp)
	intent = interpret['intent']['name']
	entities = interpret['entities']
	#print(interpret)
	entity = []
	for i in range(len(entities)):
		#entity.append([entities[i]['value'], entities[i]['start'], entities[i]['end']])
		entity.append(entities[i]['value'])

	#print(intent, entity)
	
	if intent == 'non-spoiler':
		print("Interpret the intent to be :: {}. Detected terms are :: {}".format(colored(intent, 'green'), colored(entity, 'green')))
	if intent == 'spoiler':
		print("Interpret the intent to be :: {}. Detected terms are :: {}".format(colored(intent, 'red'), colored(entity, 'red')))
