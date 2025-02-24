#embed from
#https://github.com/phaylali/omnibot-discord/blob/main/utils/kick_monitor.py
# edit kickc.json
import aiohttp
import asyncio
import json
from datetime import datetime

class KickMonitor:
    def __init__(self):
        self.monitored_channels = {}
        self.data_file = 'kickc.json'
        self.base_url = "https://kick.com/api/v1"
        self.load_channels()

    def load_channels(self):
        try:
            with open(self.data_file, 'r') as f:
                self.monitored_channels = json.load(f)
        except FileNotFoundError:
            self.monitored_channels = {}

    def save_channels(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.monitored_channels, f, indent=4)

    async def check_live_status(self, username):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/channels/{username}"
            headers = {
                'Accept': 'application/json'
            }
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    is_live = data.get('livestream') is not None
                    return is_live, data if is_live else None
                return False, None

    async def monitor_channel(self, username):
        print(f"Monitoring channel: {username}...")
        while True:
            is_live, data = await self.check_live_status(username)
            if is_live:
                print(f"{username} is LIVE! Check out the stream.")
                self.monitored_channels[username] = data
                self.save_channels()
            else:
                print(f"{username} is offline.")
            await asyncio.sleep(60)

    async def monitor_channels(self):
        tasks = [self.monitor_channel(username) for username in self.monitored_channels]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    monitor = KickMonitor()
    monitor.monitored_channels.update({
        "classybeef": None, #none consistant
        "asapgemmy": None, #or consistant usage 
    })
    monitor.save_channels()
    asyncio.run(monitor.monitor_channels())
