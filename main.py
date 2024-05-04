import tls_client


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
        session = tls_client.Session(client_identifier="chrome_124")
        build_url = "https://discord.com/assets/84471.3244a3093dadec43fc23.js"
        response = session.get(build_url, headers=headers)
        build_number = response.text.split('"buildNumber",(_="')[1].split('"')[0]
        session.close()
        return build_number
    except Exception:
        return 289814


discord_build_number = get_build_number()
print(discord_build_number)
