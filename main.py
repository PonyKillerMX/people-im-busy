"""
Example:  python3 main.py --names=mama,nelly --message="<message>"
"""
import click
# to use os.getenv from .env
import os 
# load my .env file to use. 
from dotenv import load_dotenv
# import API rest architecture 
from twilio.rest import Client

# twillio account sid
account_sid = "TWILIO-ACCOUNT-SID"
# load my auth token from .env file.
load_dotenv()
auth_token = os.getenv("auth_token")  
client = Client(account_sid, auth_token) 

# remember this has to be a confirmed number in Twilio sandbox. 
confirmed_numbers = {
                        "<name of person>": "<phone number", 
                        # add more here. 
                    }

twilio_number = "YOUR TWILIO PHONE NUMBER"


@click.command()
@click.option("--names", default=False, help="list of names separated by commas") 
@click.option("--message", default=False, help="What message do you want to send") 

def receive_args(names, message): 
    """Receive arguments provided when calling program"""
    list_names_received = names.split(',') 
    check_if_user_registered(list_names_received, message) 
   

def check_if_user_registered(list_names_received, message): 
    """Check if names provided are registered"""
    send_to = []
    # check if chosen_number in list_confirmed_numbers: 
    for x in range(len(list_names_received)): 
        if list_names_received[x] in confirmed_numbers.keys(): 
            send_to.append(list(confirmed_numbers.values())[x])
    send_message_to(send_to, message)  


def send_message_to(send_to, message): 
    """Receive the purified list and the message and send those messages"""
    # loop to send the message to different contacts: 
    for x in range(0, len(send_to)): 
        received = client.messages.create(
                                    from_=f"whatsapp:{twilio_number}",
                                    body=message,
                                    to=f"whatsapp:{send_to[x]}"
                                )
        print(f"Message sent to {send_to[x]} | token: {received.sid}")


receive_args() 


