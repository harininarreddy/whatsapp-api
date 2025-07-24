import os
import requests
from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
CLIENT_PHONE_NUMBER = os.getenv("CLIENT_PHONE_NUMBER")
url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Message payload
data = {
    "messaging_product": "whatsapp",
    "to": CLIENT_PHONE_NUMBER,
    "type": "text",
    "text": {
        "body": "Hello! WhatsApp API message sent successfully."
    }
}
try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    print("✅ Message sent successfully!")
    print("📨 Response:", response.json())
except requests.exceptions.HTTPError as errh:
    print("❌ HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("❌ Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("❌ Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("❌ Unexpected Error:", err)
