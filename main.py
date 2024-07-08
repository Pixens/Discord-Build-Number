import re

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
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}

session = tls_client.Session(client_identifier="chrome_124")


def extract_asset_files():
    request = session.get("https://discord.com/login", headers=headers)
    pattern = r'<script\s+src="([^"]+\.js)"\s+defer>\s*</script>'
    matches = re.findall(pattern, request.text)
    return matches


def get_build_number():
    try:
        files = extract_asset_files()
        for file in files:
            build_url = f"https://discord.com{file}"
            response = session.get(build_url, headers=headers)
            if "buildNumber" not in response.text:
                continue
            else:
                build_number = response.text.split('build_number:"')[1].split('"')[0]
                break

        session.close()
        return build_number
    except Exception as e:
        return 307749


discord_build_number = get_build_number()
print(discord_build_number)
