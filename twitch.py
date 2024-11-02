import json
import requests

client_id = ""
oauth_token = ""

username = ""
user_id = ""

url = f'https://api.twitch.tv/helix/streams?user_id={user_id}'
status = 1

try:
    response = requests.get(url, headers={
        "Client-ID": client_id,
        "Authorization": oauth_token
    }, timeout=15)
    response.raise_for_status()

    info = response.json()
    if info['data']:
        status = 0
    else:
        status = 1

except requests.exceptions.HTTPError as e:
    if e.response.status_code in {404, 422}:
        status = 2
    else:
        print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request error occurred: {e}")

if status == 0:
    print(f"{username} is live")
elif status == 1:
    print(f"{username} is offline")
elif status == 2:
    print("Error: User not found or invalid request.")
