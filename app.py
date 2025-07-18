import os

ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")

CLIENT_PHONE_NUMBER = 'recipient_whatsapp_number_with_country_code' 
url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": CLIENT_PHONE_NUMBER,
    "type": "text",
    "text": {
        "body": "Hello! Whats App API."
    }
}
response = requests.post(url, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
