import requests

def check_live_status(channel_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&eventType=live&type=video"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            print("livestream on")
        else:
            print("not")
    else:
        print("error:", response.status_code, response.text)

CHANNEL_ID = ""
API_KEY = ""

check_live_status(CHANNEL_ID, API_KEY)
