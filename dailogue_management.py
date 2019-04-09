from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
import warnings
import ruamel.yaml
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)


from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig


logger = logging.getLogger(__name__)

# this will catch predictions the model isn't very certain about
# there is a threshold for the NLU predictions as well as the action predictions

fallback = FallbackPolicy(fallback_action_name="utter_unclear",
                          core_threshold=0.2,
                          nlu_threshold=0.1)

def train_dialogue(domain_file = 'resto_domain.yml',
                   model_path = 'D:/RasaBot/nlu_model/dialogue',
                   training_data_file = 'D:/RasaBot/data/stories.md'):
    
    agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy(), fallback])

    data = agent.load_data(training_data_file)

    agent.train(data)

    agent.persist(model_path)

    return agent
	
def run_bot(serve_forever=True):

    interpreter = RasaNLUInterpreter('D:/RasaBot/nlu_model/default/resto_nlu')

    #endpoint = 'D:/RasaBot/endpoints'

    #action_endpoint = EndpointConfig(url= "http://localhost:5004/webhook/")

    model_path = 'D:/RasaBot/nlu_model/dialogue'

    agent = Agent.load(model_path, interpreter = interpreter)

    #rasa_core.run.serve_application(agent ,channel='cmdline')

    return agent
	
if __name__ == '__main__':
    train_dialogue()
    run_bot()
