from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


'''
Architecture:  how do we make hierarchical conversation?

For example:
        User : I am searching for a restaurant
	bot: In which location ?
	User : Hyderabad
	bot: which cuisine?
	User : Chinese.
	bot: Sure. Here is the restaurant suitable for you.
'''


class ActionRestaurant(Action):
        def name(self):
                return "action_restaurant"

        def run(self, dispatcher, tracker, domain):

                loc = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                
                restaurant_name = "Bowl O'China"

                response = """The {} is the {} restaurant available in {} """.format(restaurant_name, cuisine, loc )

                dispatcher.utter_message(response)
