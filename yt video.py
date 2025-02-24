#new video
#pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

import googleapiclient.discovery
import googleapiclient.errors
import time

API_KEY = 'YOUR_API_KEY'
CHANNEL_ID = 'CHANNEL_ID_OF_THE_YOUTUBER'

def get_youtube_service():
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=API_KEY
    )
    return youtube

def get_latest_video(youtube, channel_id):
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        order="date",
        maxResults=1
    )
    response = request.execute()
    latest_video = response['items'][0]
    video_title = latest_video['snippet']['title']
    video_url = f"https://www.youtube.com/watch?v={latest_video['id']['videoId']}"
    return video_title, video_url

def check_for_new_video():
    youtube = get_youtube_service()
    latest_video_title, latest_video_url = get_latest_video(youtube, CHANNEL_ID)
    print(f"new video \n제목: {latest_video_title} \n링크: {latest_video_url}")

while True:
    check_for_new_video()
    time.sleep(10)
