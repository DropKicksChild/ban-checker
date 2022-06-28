import requests
import time
from discord_webhook import DiscordWebhook

key = ' ' #hypixel api key
webhook = ' ' #discord webhook
checkDelay = 3000 #in ms

def staff():
    global oldBans, webhook
    a = requests.get(f'https://api.hypixel.net/punishmentstats?key={key}').json()
    oldBans = (a['staff_total'])
    while True:
        r = requests.get(f'https://api.hypixel.net/punishmentstats?key={key}').json()
        newBans = (r['staff_total'])
        print(newBans)

        lastMinute = newBans - oldBans
        webhook = DiscordWebhook(url=f'{webhook}', content=f'Staff have banned {lastMinute} people since the last check')
        response = webhook.execute()
        print(lastMinute)
        oldBans = newBans
        time.sleep(checkDelay)


staff()
