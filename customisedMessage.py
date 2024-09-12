import pandas as pd
import pywhatkit as kit
import time
import pyautogui

# Load the Excel file
file_path = "contacts.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)

# Define the message template
message_template = """
Dear {name},

lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus ut sem malesuada tincidunt. lorem ipsum dolor sit amet, consectetur adipiscing elit. Null
"""

# Iterate through the contact list and send WhatsApp messages
for index, row in data.iterrows():
    try:
        name = row['Name']
        
        phone_number = str(row['Phone Number']).strip()  # Convert to string and remove any leading/trailing spaces

        # Ensure the phone number starts with a '+' (country code is included)
        if not phone_number.startswith("+"):
            phone_number = "+" + phone_number

        # Personalize the message
        personalized_message = message_template.format(name=name)

        # Send the message using pywhatkit (open WhatsApp Web and send the message)
        print(f"Sending message to {name} at {phone_number}...")

        kit.sendwhatmsg_instantly(phone_number, personalized_message, wait_time=15, tab_close=True)

        # Add a delay to let the message send and prevent being blocked by WhatsApp
        time.sleep(5)

        # Close the WhatsApp web tab using pyautogui to avoid multiple open tabs
        pyautogui.hotkey('ctrl', 'w')  # Close the browser tab

        # Pause between messages to avoid rate limiting
        time.sleep(10)


    except Exception as e:
        print(f"Error sending message to {name} at {phone_number}: {e}")
        continue
