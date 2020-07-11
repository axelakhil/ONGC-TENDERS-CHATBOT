# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionShowByID(Action):

    def name(self) -> Text:
        return "action_show_by_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        eeid=tracker.get_slot("tend")
        
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM employees where Tender_number='{}'".format(eeid))
        rows = cursorObj.fetchall()
        if(rows==[]):
            dispatcher.utter_message("No Tender with this ID is found.Please check again its case sensitive")
        else:
            for row in rows:
                dispatcher.utter_message("Tender Number:{}\n Tender_name: {}\n Tender_type:{}\n Last_date :{} \n Location:{}\n".format(row[0],row[1],row[2],row[3],row[4]))
        return []

class ActionShowAll(Action):

    def name(self) -> Text:
        return "action_show_by_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cat=tracker.get_slot("tender")
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM employees where Tender_type='{}'".format(cat))
        rows = cursorObj.fetchall()
        if(rows==[]):
            dispatcher.utter_message("No such tender category is found.Please check again its case sensitive(1.e-gas 2.Procurement 3.Corrigendum)")
    
            for row in rows:
                dispatcher.utter_message("Tender Number:{}\n Tender_name: {}\n Tender_type:{}\n Last_date :{} \n Location:{}\n".format(row[0],row[1],row[2],row[3],row[4]))


        return []