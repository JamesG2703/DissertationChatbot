# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import os
from pathlib import Path
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
import requests
# from weather import Weather
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client
from rasa_sdk.types import DomainDict

# class ActionHelloWorld(Action):

#      def name(self) -> Text:
#          return "action_weather_api"

#      def run(self, dispatcher: CollectingDispatcher,
#      tracker: Tracker,
#      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#          city=tracker.latest_message['text']
#          temp=int(Weather(city)['temp']-273)
#          dispatcher.utter_template("utter_temp",
#             tracker,temp=temp)

#          return []

class ActionEmailSubmit(Action):
    def name(self) -> Text:
        return "action_email_submit"
    
    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

       SendEmail(
           tracker.get_slot("email"),
           tracker.get_slot("subject"),
           tracker.get_slot("message")
       )
       dispatcher.utter_message("Thanks for providing the details. We have sent you an email at {}".format(tracker.get_slot("email")))
       return True

def SendEmail(toaddr,subject,message):
    fromaddr = "jamesxbox720@gmail.com"
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

     # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    try:
        s.login(fromaddr, "UnitedBritain2021")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
    except:
        print("An Error occured while sending email.")
    finally:
        # terminating the session
        s.quit()
        return []

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        account_sid = 'ACe20d5a54e3768db915ab7eb693f1473b'
        auth_token = '0c0d99f13c5288b558d1890f9b214efb'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+12057198793',
            body=tracker.get_slot("message_sms"),  #'hello, this is a test message for automation',
            to = tracker.get_slot("mobile_number")     # '+918209829808'
        )

        print(message.sid)

        dispatcher.utter_message(text="Message has been sent successfully to {}".format(tracker.get_slot("mobile_number")))

        return []

# Creating new class to send emails.
class ActionEmail(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_email"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        name = tracker.get_slot("name")
        email_id = tracker.get_slot("email_id")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "Hello {} , thank you for signing up to our newsletter!".format(name)
    
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", email_id, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionCashRefund(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_cash_refund"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        refund_cash_reciept_no = tracker.get_slot("refund_cash_reciept_no")
        refund_cash_reciept_email = tracker.get_slot("refund_cash_reciept_email")
        refund_cash_reciept_reason = tracker.get_slot("refund_cash_reciept_reason")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "Your reciept number is {}\nWe will let you know if you are eligible and will be recieving a refund via your reason: {}".format(refund_cash_reciept_no, refund_cash_reciept_reason)
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", refund_cash_reciept_email, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionCardRefund(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_card_refund"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        refund_card_reciept_no = tracker.get_slot("refund_card_reciept_no")
        refund_card_bank_no = tracker.get_slot("refund_card_bank_no")
        refund_card_sort_code_no = tracker.get_slot("refund_card_sort_code_no")
        refund_card_reciept_email = tracker.get_slot("refund_card_reciept_email")
        refund_card_reason = tracker.get_slot("refund_card_reason")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "Your reciept number is {}\nWe will let you know if you are eligible and will be recieving a refund via your reason: {}\nBank Details - Card Number: {}, Sort Code: {}".format(refund_card_reciept_no, refund_card_reason, refund_card_bank_no, refund_card_sort_code_no)
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", refund_card_reciept_email, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionPayPalRefund(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_paypal_refund"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        refund_paypal_reciept_no = tracker.get_slot("refund_paypal_reciept_no")
        refund_paypal_card_bank_no = tracker.get_slot("refund_paypal_card_bank_no")
        refund_paypal_sort_code_no = tracker.get_slot("refund_paypal_sort_code_no")
        refund_paypal_email = tracker.get_slot("refund_paypal_email")
        refund_paypal_reason = tracker.get_slot("refund_paypal_reason")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "Your reciept number is {}\nWe will let you know if you are eligible and will be recieving a refund via your reason: {}\nPaypal Details - Paypal Card Number: {}, Paypal Sort Code: {}".format(refund_paypal_reciept_no, refund_paypal_reason, refund_paypal_card_bank_no, refund_paypal_sort_code_no)
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", refund_paypal_email, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionChangeEmailWithPassword(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_change_email_password_route"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        # email_change_password = tracker.get_slot("email_change_password")
        old_email_password_change = tracker.get_slot("old_email_password_change")
        new_email_password_change = tracker.get_slot("new_email_password_change")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "Your email address has now been changed with the use of your password!\n\nOld Email: {}\n\nNew Email: {}".format(old_email_password_change, new_email_password_change)
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", new_email_password_change, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionChangeEmailWithSecretQuestion(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_change_email_secret_question_route"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        # email_change_password = tracker.get_slot("email_change_password")
        email_change_secret_question = tracker.get_slot("email_change_secret_question")
        old_email_secret_question_change = tracker.get_slot("old_email_secret_question_change")
        new_email_secret_question_change = tracker.get_slot("new_email_secret_question_change")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "Your email address has now been changed with the use of your secret question!\n\nAnswer to Secret Question: {}\n\nOld Email: {}\n\nNew Email: {}".format(email_change_secret_question, old_email_secret_question_change, new_email_secret_question_change)
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", new_email_secret_question_change, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionChangePasswordWithOldPassword(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_change_password_password_route"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        password_email_password_change = tracker.get_slot("password_email_password_change")
        old_password_password_change = tracker.get_slot("old_password_password_change")
        new_password_password_change = tracker.get_slot("new_password_password_change")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "You have successfully changed your password with the use of your old password!\n\nOld Password: {}\n\nNew Password:{}".format(old_password_password_change, new_password_password_change)
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", password_email_password_change, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionChangePasswordWithSecretQuestion(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_change_password_secret_question_route"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        password_email_secret_question_change = tracker.get_slot("password_email_secret_question_change")
        password_change_secret_question = tracker.get_slot("password_change_secret_question")
        new_password_secret_question = tracker.get_slot("new_password_secret_question")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("jamesxbox720@gmail.com", "UnitedBritain2021")
          
        # Message to be sent
        message = "You have successfully changed your password with the use of a secret question!\n\nSecret Question Answer: {}\n\nNew Password:{}".format(password_change_secret_question, new_password_secret_question)
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID", password_email_secret_question_change, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionChangePhoneNumberWithPassword(Action):

    def name(self) -> Text:
        return "action_change_phone_number_password_route"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        account_sid = 'ACe20d5a54e3768db915ab7eb693f1473b'
        auth_token = '0c0d99f13c5288b558d1890f9b214efb'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+12057198793',
            body = "You have successfully changed your phone number with your password!",  #'hello, this is a test message for automation',
            to = tracker.get_slot("new_mobile_number_password_change")     # '+918209829808'
        )

        print(message.sid)

        dispatcher.utter_message(text="Message has been sent successfully to {}".format(tracker.get_slot("new_mobile_number_password_change")))

        return []

class ActionChangePhoneNumberWithSecretQuestion(Action):

    def name(self) -> Text:
        return "action_change_phone_number_secret_password_route"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        account_sid = 'ACe20d5a54e3768db915ab7eb693f1473b'
        auth_token = '0c0d99f13c5288b558d1890f9b214efb'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+12057198793',
            body = "You have successfully changed your phone number with your secret question!",  #'hello, this is a test message for automation',
            to = tracker.get_slot("new_mobile_number_secret_question_change")     # '+918209829808'
        )

        print(message.sid)

        dispatcher.utter_message(text="Message has been sent successfully to {}".format(tracker.get_slot("new_mobile_number_secret_question_change")))

        return []

# class ActionHaystack(Action):

#     def name(self) -> Text:
#         return "call_haystack"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         url = "http://localhost:8000/query"
#         payload = {"query": str(tracker.latest_message["text"])}
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         response = requests.request("POST", url, headers=headers, json=payload).json()

#         if response["answers"]:
#             answer = response["answers"][0]["answer"]
#         else:
#             answer = "No Answer Found!"

#         dispatcher.utter_message(text=answer)

#         return []