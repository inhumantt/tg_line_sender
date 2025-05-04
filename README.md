# tg_line_sender

This script monitors two text files for new lines and sends those lines as messages to a specified Telegram chat using a bot. It checks the files every 15 minutes, ensuring no duplicate messages are sent.

## Features

- Monitors two text files for new content.
- Sends messages to a Telegram chat when new lines are added to the files.
- Avoids sending duplicate messages.
- Periodically checks the files every 15 minutes.

## Requirements

- Python 3.x
- `requests` library (for sending HTTP requests to the Telegram API)

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/telegram-sender-template.git
cd telegram-sender-template
2. Install the required dependencies:
bash
Copy
Edit
pip install requests
3. Update the script with your Telegram bot token and chat ID:
Replace the following placeholders in the script with your actual values:

TELEGRAM_BOT_TOKEN: Your bot token from BotFather.

TELEGRAM_CHAT_ID: Your Telegram channel or group chat ID (can be obtained from your bot or a Telegram group chat).

python
Copy
Edit
TELEGRAM_BOT_TOKEN = "Your bot token here"
TELEGRAM_CHAT_ID = "Your channel/group ID here"
4. Customize the file names:
In the script, you can adjust the FILE_1 and FILE_2 variables to reflect the names of the text files you want to monitor.

python
Copy
Edit
FILE_1 = "file1.txt"
FILE_2 = "file2.txt"
5. Run the script:
bash
Copy
Edit
python telegram_sender_template.py
The script will start running and check the files every 15 minutes. Any new lines added to the files will be sent as messages to your specified Telegram chat.

How It Works
The script reads lines from the two specified text files (file1.txt and file2.txt).

It sends any new lines (that haven't been sent before) to the specified Telegram chat.

The script checks the files every 15 minutes to send any new lines.

It avoids sending duplicate lines by keeping track of what has already been sent.

Customize the Labels
You can customize the label for each file in the script. By default, the labels are:

"Found from file1" for file1.txt

"Found from file2" for file2.txt

These labels are used as part of the message sent to Telegram. Modify the process_file function to change the label for each file.

Example Usage
Add new lines to file1.txt or file2.txt.

Wait for the script to check the files every 15 minutes.

Any new lines will be sent to the Telegram chat you specified.

License
This project is licensed under the MIT License - see the LICENSE file for details.

csharp
Copy
Edit

Simply copy and paste this content into a `README.md` file in your GitHub repository!
