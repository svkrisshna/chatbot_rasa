from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configuration, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configuration))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'resto_nlu')


def run_nlu():
    interpreter = Interpreter.load('D:/RasaBot/nlu_model/default/resto_nlu')
    print(interpreter.parse(u"I am planning a dinner with my parents, suggest some restaurants anywhere in the west"))


if __name__ == '__main__':
    train_nlu('D:/RasaBot/data/data.json', 'config_spacy.json', 'D:/RasaBot/nlu_model')
    #model_directory = train_nlu('D:/RasaBot/data/data.json', 'config_spacy.json', 'D:/RasaBot/nlu_model')
    run_nlu()
    
