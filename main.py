import requests
import re
import json
import time


def get_build_number():
    build_number = 253927
    try:
        file = 'https://discord.com/assets/sentry.45a9e80f852893c9e895.js'
        file_response = requests.get(file)
        build_number = file_response.text.split('buildNumber",(t="')[1].split('"')[0]
    except Exception as e:
        pass
        
    return int(build_number)

discord_build_number = get_build_number()
print(discord_build_number)
