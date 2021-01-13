"""This is the main folder to implement the application
Example: 
    >>> people-im-busy message mama, nelly "<message>"
"""

from dotenv import load_dotenv
# import API rest architecture 
from twilio.rest import Client

# twillio account sid
account_sid = 'AC1e9568a7617477ad8eae52edd3c61fb6' 

# load my auth token from .env file.
load_dotenv()
auth_token = os.getenv("auth_token")  

client = Client(account_sid, auth_token) 

verified_numbers = []
chosen_numbers = "GRAB FROM ARGUMENTS"
# check if chosen_number in list_confirmed_numbers: 
for x in range(len(confimed_numbers)): 
    if chosen_numbers[x] in confirmed_numbers: 
        verified_numbers.append(chosen_number)



# What numbers are actually verified from the ones you want to send? 
print(verified_numbers) 


# for loop to send the message to different contacts: 
for x in range(len(send_to)): 
    message = client.message.create(
                                from_="whatsapp:+14155238886",
                                body=chosen_body,
                                to="whatsapp:+523318934771"
                                #to=verified_numbers[x],

                            )

# show what happened
print(message.sid)
