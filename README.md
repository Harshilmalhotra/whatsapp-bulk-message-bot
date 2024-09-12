# WhatsApp Message Automation using Python

This project allows you to automate sending bulk messages on WhatsApp using Python. You can send the same message to multiple recipients listed in an Excel file. This is particularly useful for sending announcements, invitations, or any mass communication without the need for manual input.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Excel File Format](#excel)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Bulk Messaging**: Automatically send messages to multiple WhatsApp contacts.
- **Excel Integration**: Load contact names and numbers directly from an Excel file.
- **WhatsApp Web Automation**: Leverages `pywhatkit` to send messages via WhatsApp Web.
- **Tab Management**: Automatically closes WhatsApp Web tabs after sending each message.
- **Error Handling**: Skips any invalid numbers and continues sending messages to other recipients.

## Installation

Follow these basic steps to install and run the project.

#### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Harshilmalhotra/whatsapp-bulk-message-bot.git
cd whatsapp-bulk-message-bot
```

#### 2. Install Python

Make sure you have **Python 3.x** installed on your system. If not, you can download it [here](https://www.python.org/downloads/).

#### 3. Install Required Python Packages

Install the required Python libraries using `pip`:

```bash
pip install pandas pywhatkit pyautogui openpyxl
```

## Required Python Packages

- **pandas**: For reading and working with Excel files.
- **pywhatkit**: To send messages via WhatsApp.
- **pyautogui**: To close browser tabs.
- **openpyxl**: For Excel file operations.

## 4. Excel File Format

Create an Excel file named `contacts.xlsx` in the root directory of the project. This file should contain the contact names and phone numbers.

### Example of Excel file:

| Name     | Phone Number   |
|----------|----------------|
| John Doe | +1234567890    |
| Jane Roe | +0987654321    |

**Important**: Make sure the phone numbers include the country code (e.g., +1 for the US).

---

## Usage

Once you have installed the required dependencies and prepared your Excel file, you can run the script:

```bash
python <ilename>.py
```

## Troubleshooting
- Invalid Phone Numbers: Ensure that all phone numbers start with a + and the correct country code. The script will skip invalid numbers and move on to the next one.
- Rate Limiting: Avoid sending too many messages too quickly to prevent WhatsApp from blocking your number. If you're sending a large volume of messages, consider adding a delay between each send (e.g., time.sleep(5)).
- Browser Not Closing: If the browser tab doesn't close automatically, make sure pyautogui is installed and that your browser allows automated keyboard inputs.

## Contributing
If you have suggestions or want to contribute to this project, feel free to open an issue or submit a pull request.

