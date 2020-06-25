import rasa.nlu
import rasa.core
import spacy
import pandas as pd 
import regex as re 

from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer, Interpreter 
from rasa.nlu import config 

interpreter = Interpreter.load("./models/nlu/disaster_v2")
df = pd.read_csv(r"test.csv")
TEXT = df['text']
ID = df['id']

tex = []
def subsi(te):
	text_cleaned = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",te).split())
	return(text_cleaned)

for text in TEXT:
	cl = subsi(text)
	tex.append(cl)

df['text'] = tex
df['text'] = df['text'].str.lower()
df = df[['id', 'text']]
print(df.head(19))


#inp = df['text'].astype(str)
target = []
counter = 0
for te in tex:
	counter = counter+1
	interpret = interpreter.parse(te)
	targ = interpret['intent']['name']
	target.append(targ)
	print(f"On question number :: {counter} out of {len(df)}")
df['target'] = target
df = df[['id', 'target']]
df.to_csv("submit_this.csv", index = False)

