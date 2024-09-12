import pandas as pd
import pywhatkit as kit
import time
import pyautogui

# Load the Excel file
file_path = "contacts.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)

# Define the message to be sent (No customization, same message for everyone)
message = """
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   your message here  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

"""

# Iterate through the contact list and send WhatsApp messages
for index, row in data.iterrows():
    try:
        phone_number = str(row['Phone Number']).strip()  # Convert to string and remove any leading/trailing spaces

        # Ensure the phone number starts with a '+' (country code is included)
        if not phone_number.startswith("+"):
            phone_number = "+" + phone_number

        # Send the message using pywhatkit (open WhatsApp Web and send the message)
        print(f"Sending message to {phone_number}...")

        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)

        # Close the WhatsApp web tab using pyautogui to avoid multiple open tabs
        pyautogui.hotkey('ctrl', 'w')  # Close the browser tab

        # Short delay between messages to ensure smooth operation
        time.sleep(5)

    except Exception as e:
        print(f"Error sending message to {phone_number}: {e}")
        continue
