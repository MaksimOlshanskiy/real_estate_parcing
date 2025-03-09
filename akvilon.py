import requests

cookies = {
    '_ym_uid': '1741077827663790128',
    '_ym_d': '1741077827',
    'tmr_lvid': 'bb2c6be56324302c0ee8ce3d786cc1bd',
    'tmr_lvidTS': '1741077826623',
    '_ym_isad': '2',
    'cted': 'modId%3Daymg2z1m%3Bya_client_id%3D1741077827663790128',
    '_ymab_param': 'JMebkXaUKvcOLMfVMEH7aVFEGGtP77O6U9X-DX7ZuU1iTCDto2NnmLg6GNW4ABvqlvUvmEvyO63OsqMe3yyFmpZPHgQ',
    'scbsid_old': '2725937795',
    'domain_sid': 'H3vsaC0Nj18jRojThU9-z%3A1741077836124',
    '_ct_ids': 'aymg2z1m%3A52820%3A2116017802',
    '_ct_session_id': '2116017802',
    '_ct_site_id': '52820',
    '_ct': '800000000945999042',
    '_ct_client_global_id': 'fbe0ef66-3f93-5e30-a689-c3153a19a53a',
    'sma_session_id': '2211334232',
    'SCBfrom': 'https%3A%2F%2Fgroup-akvilon.ru%2F',
    'smFpId_old_values': '%5B%228ffe7a1c09dffb649545b8fc0287fbcd%22%5D',
    'city': '2',
    'accept-cookie': 'true',
    'call_s': '___z6mfuoam.1741079626.554487128.188298:578564|d6e6c8d2.1741079626.3558282052.24446:319232|aymg2z1m.1741080359.2116017802.258214:781696|2___',
    'tmr_detect': '0%7C1741078561712',
    'sma_index_activity': '15499',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://msk.group-akvilon.ru/project/akvilon-signal/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': '_ym_uid=1741077827663790128; _ym_d=1741077827; tmr_lvid=bb2c6be56324302c0ee8ce3d786cc1bd; tmr_lvidTS=1741077826623; _ym_isad=2; cted=modId%3Daymg2z1m%3Bya_client_id%3D1741077827663790128; _ymab_param=JMebkXaUKvcOLMfVMEH7aVFEGGtP77O6U9X-DX7ZuU1iTCDto2NnmLg6GNW4ABvqlvUvmEvyO63OsqMe3yyFmpZPHgQ; scbsid_old=2725937795; domain_sid=H3vsaC0Nj18jRojThU9-z%3A1741077836124; _ct_ids=aymg2z1m%3A52820%3A2116017802; _ct_session_id=2116017802; _ct_site_id=52820; _ct=800000000945999042; _ct_client_global_id=fbe0ef66-3f93-5e30-a689-c3153a19a53a; sma_session_id=2211334232; SCBfrom=https%3A%2F%2Fgroup-akvilon.ru%2F; smFpId_old_values=%5B%228ffe7a1c09dffb649545b8fc0287fbcd%22%5D; city=2; accept-cookie=true; call_s=___z6mfuoam.1741079626.554487128.188298:578564|d6e6c8d2.1741079626.3558282052.24446:319232|aymg2z1m.1741080359.2116017802.258214:781696|2___; tmr_detect=0%7C1741078561712; sma_index_activity=15499',
}

params = {
    'project': '37098',
    'order': 'price',
    'limit': 5
}

response = requests.get('https://msk.group-akvilon.ru/api/flats/', params=params, cookies=cookies, headers=headers)

items = response.json()["results"]

for i in items:
    project = i["project_title"]
    room_id = i["id"]
    price = i["price"]
    print(project, id, price)