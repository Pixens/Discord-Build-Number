import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "https://discord.com/login",
    "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


def get_build_number():
    try:
        build_url = "https://discord.com/assets/84471.60c6151c70426311ebdb.js"
        response = requests.get(build_url, headers=headers)
        build_number = response.text.split('"buildNumber",(_="')[1].split('"')[0]
        return build_number
    except Exception:
        return 289814


discord_build_number = get_build_number()
print(discord_build_number)
