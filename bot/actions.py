# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, ReminderScheduled
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from connections.database import Database

import random


class MeasurementForm(FormAction):

    def name(self) -> Text:

        return "measurement_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["weight", "bodyfatratio"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "weight": self.from_entity(entity="number", not_intent="chitchat"),
            "bodyfatratio": self.from_entity(entity="number", not_intent="chitchat"),

            # "bodyfatratio": [
            #     self.from_entity(
            #         entity="bodyfatratio", intent=["inform", "request_restaurant"]
            #     ),
            #     self.from_entity(entity="number"),
            # ],
            # "outdoor_seating": [
            #     self.from_entity(entity="seating"),
            #     self.from_intent(intent="affirm", value=True),
            #     self.from_intent(intent="deny", value=False),
            # ],
            # "preferences": [
            #     self.from_intent(intent="deny", value="no additional preferences"),
            #     self.from_text(not_intent="affirm"),
            # ],
            # "feedback": [self.from_entity(entity="feedback"), self.from_text()],
        }

    @staticmethod
    def is_number(string: Text) -> bool:
        try:
            float(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    # def validate_cuisine(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Optional[Text]:
    #     """Validate cuisine value."""
    #
    #     if value.lower() in self.cuisine_db():
    #         # validation succeeded, set the value of the "cuisine" slot to value
    #         return {"cuisine": value}
    #     else:
    #         dispatcher.utter_template("utter_wrong_cuisine", tracker)
    #         # validation failed, set this slot to None, meaning the
    #         # user will be asked for the slot again
    #         return {"cuisine": None}
    #
    # def validate_num_people(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Optional[Text]:
    #     """Validate num_people value."""
    #
    #     if self.is_int(value) and int(value) > 0:
    #         return {"num_people": value}
    #     else:
    #         dispatcher.utter_template("utter_wrong_num_people", tracker)
    #         # validation failed, set slot to None
    #         return {"num_people": None}
    #
    # def validate_outdoor_seating(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Any:
    #     """Validate outdoor_seating value."""
    #
    #     if isinstance(value, str):
    #         if "out" in value:
    #             # convert "out..." to True
    #             return {"outdoor_seating": True}
    #         elif "in" in value:
    #             # convert "in..." to False
    #             return {"outdoor_seating": False}
    #         else:
    #             dispatcher.utter_template("utter_wrong_outdoor_seating", tracker)
    #             # validation failed, set slot to None
    #             return {"outdoor_seating": None}
    #
    #     else:
    #         # affirm/deny was picked up as T/F
    #         return {"outdoor_seating": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        print(tracker.get_slot("bodyfatratio"))
        user_id = tracker.get_slot("user_id")
        weight = tracker.get_slot("weight")
        bodyfatratio = tracker.get_slot("bodyfatratio")
        db = Database.get_instance()
        db.add_measurements(user_id, weight, bodyfatratio)
        # utter submit template
        return []


class SetName(Action):
    def name(self):
        return "action_set_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot("PERSON").title()

        return [SlotSet("user_name", user_name)]


class ConfirmUserWantsRoutine(Action):
    def name(self):
        return "action_confirm_user_wants_routine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("wants_routine", True)]


class ConfirmUserWantsDiets(Action):
    def name(self):
        return "action_confirm_user_wants_diets"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("wants_diets", True)]


class ConfirmUserWantsMeasurements(Action):
    def name(self):
        return "action_confirm_user_wants_measurements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("measure_user", True)]


class SetBirthdate(Action):
    def name(self):
        return "action_set_birthdate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        birthdate = tracker.get_slot("time")[0:10]
        year = tracker.get_slot("time")[0:5]
        print(year)
        if year == "2019":
            return []

        return [SlotSet("birthdate", birthdate)]


class AddUser(Action):
    def name(self):
        return "action_add_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot("user_name")
        birthdate = tracker.get_slot("birthdate")
        user_gender = tracker.get_slot("user_gender")
        telegram_id = tracker.sender_id
        training_type = tracker.get_slot("training_type")
        measure_user = tracker.get_slot("measure_user")

        db = Database.get_instance()
        db.add_user(telegram_id, user_name, birthdate, user_gender, training_type, measure_user)
        user_id = db.get_user_id(telegram_id)
        return [SlotSet("user_id", user_id)]


class CheckProfile(Action):
    def name(self):
        return "action_check_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        db = Database.get_instance()
        user_exists, user_id, user_name, user_gender, measure_user = db.check_user_exists(
            tracker.sender_id)
        return [SlotSet("user_exists", user_exists),
                SlotSet("user_name", user_name),
                SlotSet("measure_user", measure_user),
                SlotSet("user_gender", user_gender),
                SlotSet("user_id", user_id)]


class ShowProgress(Action):
    def name(self):
        return "action_show_progress"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Working on showing your progress")
        return []


class MeasurementReminder(Action):
    def name(self):
        return "action_set_reminder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Working on setting reminders")
        return []


# class AddMeasurements(Action):
#     def name(self):
#         return "action_add_measurements"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         user_id = tracker.get_slot("user_id")
#         weight = tracker.get_slot("weight")
#         bodyfatratio = tracker.get_slot("bodyfatratio")
#         db = Database.get_instance()
#         db.add_measurements(user_id, weight, bodyfatratio)
#
#         return []

# class Greet(Action):
#
#     responses = ["Hey {user_name}! How are you?"]
#
#     def name(self):
#         return "action_greet"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         name = tracker.get_slot("user_name")
#         rand_response = self.responses[random.randrange(len(self.responses))]
#
#         response = rand_response.replace("{user_name}", name)
#
#         dispatcher.utter_message(response)

        return []


class GetMeasurements(Action):
    def name(self):
        return "action_get_measurements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("user_name")
        rand_response = self.responses[random.randrange(len(self.responses))]

        response = rand_response.replace("{user_name}", name)

        dispatcher.utter_message(response)

        return []


class StartTraining(Action):

    def name(self) -> Text:
        return "action_start_training"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(tracker.get_latest_input_channel())
        dispatcher.utter_message(tracker.sender_id)
        dispatcher.utter_message("Let's start training")

        return []
