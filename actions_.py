# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import psycopg2

class ActionMapFormSubmit(Action):
    def name(self) -> Text:
        return "action_map_form_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(dbname="GeochatbotDB", user="mohammad", password="geo123456", host="localhost")
        cur = conn.cursor()

        # Extract entities
        data = tracker.latest_message['entities'][0]['value'] if tracker.latest_message['entities'] else None
        location = tracker.latest_message['entities'][1]['value'] if len(tracker.latest_message['entities']) > 1 else None
        date = tracker.latest_message['entities'][2]['value'] if len(tracker.latest_message['entities']) > 2 else None

        # Fetch link to map service from database based on entities
        cur.execute("SELECT link FROM map_services WHERE data=%s AND location=%s AND date=%s", (data, location, date))
        link = cur.fetchone()[0]

        # Close database connection
        cur.close()
        conn.close()

        dispatcher.utter_message(text="Here is the link to the map service: {}".format(link))
        return []

class ActionToolFormSubmit(Action):
    def name(self) -> Text:
        return "action_tool_form_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(dbname="GeochatbotDB", user="mohammad", password="geo123456", host="localhost")
        cur = conn.cursor()

        # Extract entity
        tool = tracker.latest_message['entities'][0]['value'] if tracker.latest_message['entities'] else None

        # Fetch link to geoprocessing service from database based on entity
        cur.execute("SELECT link FROM geoprocessing_services WHERE name=%s", (tool,))
        link = cur.fetchone()[0]

        # Close database connection
        cur.close()
        conn.close()

        dispatcher.utter_message(text="Here is the link to the geoprocessing service: {}".format(link))
        return []

class ActionExpertiseFormSubmit(Action):
    def name(self) -> Text:
        return "action_expertise_form_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(dbname="GeochatbotDB", user="mohammad", password="geo123456", host="localhost")
        cur = conn.cursor()

        # Extract entity
        expertise = tracker.latest_message['entities'][0]['value'] if tracker.latest_message['entities'] else None

        # Fetch volunteer name from database based on expertise
        cur.execute("SELECT volunteer_name FROM volunteer_profiles WHERE expertise=%s", (expertise,))
        volunteer_name = cur.fetchone()[0]

        # Close database connection
        cur.close()
        conn.close()

        dispatcher.utter_message(text="The volunteer with {} expertise is: {}".format(expertise, volunteer_name))
        return []