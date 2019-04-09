from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter

logger = logging.getLogger(__name__)


def resto_test(interpreter,
               domain_file="resto_domain.yml",
               training_data_file='D:/RasaBot/data/stories.md'):

    #action_endpoint = EndpointConfig(url="http://localhost:5004/webhook")
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(),KerasPolicy()],
                  interpreter=interpreter)

    data = agent.load_data(training_data_file)
    agent.train_online(data)
    #interactive.run_interactive_learning(agent, training_data_file)

    return agent


if __name__ == '__main__':

    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('D:/RasaBot/nlu_model/default/resto_nlu')
    resto_test(nlu_interpreter)
