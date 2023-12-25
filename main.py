import requests
import re
import json
import time


#Credits to https://github.com/itschasa for this.
def get_build_number():
    try:
        login_page_request = requests.get('https://discord.com/login', headers={"Accept-Encoding": "identity"})
        login_page = login_page_request.text
        build_url = 'https://discord.com/assets/' + re.compile(r'assets/(sentry\.\w+)\.js').findall(login_page)[0] + '.js'
        build_request = requests.get(build_url, headers={"Accept-Encoding": "identity"})
        build_nums = re.findall(r'buildNumber\D+(\d+)"', build_request.text)
        return int(build_nums[0])
    except Exception:
        return 256231


discord_build_number = get_build_number()
print(discord_build_number)
