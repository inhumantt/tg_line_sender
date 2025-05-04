import os
import time
import requests

# File names (Update the file names as needed)
FILE_1 = "file1.txt"  # Name of the first text file
FILE_2 = "file2.txt"  # Name of the second text file

# Telegram credentials (Update these with your credentials)
TELEGRAM_BOT_TOKEN = "Your bot token here"  # Replace with your Telegram bot token
TELEGRAM_CHAT_ID = "Your channel/group ID here"  # Replace with your Telegram chat ID (can be a group/channel ID)

# API URL for Telegram Bot
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Store already sent lines to avoid duplicates
sent_file1 = set()
sent_file2 = set()

def send_telegram_message(text):
    """
    Sends a message to the specified Telegram chat using the bot's token.
    """
    try:
        data = {'chat_id': TELEGRAM_CHAT_ID, 'text': text}
        response = requests.post(TELEGRAM_URL, data=data)
        if response.status_code == 200:
            print(f"Sent: {text}")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending message: {e}")

def process_file(file_path, sent_lines, label):
    """
    Processes the given file and sends any new lines to Telegram.
    """
    if not os.path.exists(file_path):
        return  # Skip if the file does not exist

    # Read lines from the file and strip whitespace
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Filter out lines that have already been sent
    new_lines = [line.strip() for line in lines if line.strip() and line.strip() not in sent_lines]

    # Send new lines to Telegram
    for line in new_lines:
        send_telegram_message(f"📌 {label}: {line}")
        sent_lines.add(line)

def main():
    """
    Main function to repeatedly check the files every 15 minutes and send new lines to Telegram.
    """
    print("Telegram sender started. Checking every 15 minutes...")

    while True:
        try:
            # Process both files
            process_file(FILE_1, sent_file1, "Found from file1")
            process_file(FILE_2, sent_file2, "Found from file2")
        except Exception as e:
            print(f"Error during check: {e}")

        # Wait for 15 minutes before checking again
        time.sleep(900)

if __name__ == "__main__":
    main()
