import requests
import time
from discord_webhook import DiscordWebhook

key = '783da3cf-64e3-42cb-a17b-09c2048971a4'
webhook = 'https://discord.com/api/webhooks/972975143926239324/ffTFVr0xmoGmRSoXUtLnA1_XGSUytqVYN75KwiWUWixqG1BZyNA-ZrK6bq9zQcK9uItw'
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
