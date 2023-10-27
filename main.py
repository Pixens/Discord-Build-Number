import requests
import re
import json
import time


def get_build_number():
    build_number = 240884
    try:
        login_response = requests.get('https://discord.com/login')
        file = 'https://discord.com/assets/' + re.compile(r"assets/+([a-z0-9]+)\.js").findall(login_response.text)[-2] + '.js'
        file_response = requests.get(file)
        build_number = file_response.text.split('Build Number: ").concat("')[1].split('",')[0]
    except Exception:
        pass
        
    return int(build_number)
