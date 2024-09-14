

import requests

cookies = {
    'XSRF-TOKEN': 'eyJpdiI6Ik1xTGRaWitva1IxS2tJaW43dWdHbEE9PSIsInZhbHVlIjoiRmxUQ2twTFRHR045OXlwSTJKd3I0ZVVmTFpiTk8zd3BHanhkWjJVMG1XWkI5RGlGZDhBbkNxaHkxbGFUaEJYQyIsIm1hYyI6IjM2NzVkMjVhZjE4N2MzNDlkMWE1Y2E2OTUwZTM0MTQxY2U2MGRmYzhmNTBiODc1NDQ5OGFlZTUxNGM1MzJkMWEifQ%3D%3D',
    'exploit_database_session': 'eyJpdiI6ImhYS2JhR0piUllLQmpNeHRiOG91WVE9PSIsInZhbHVlIjoibWNmbTZGYUorcWF1TFNIWmZVRXhWbXpYOHhtNVZqQnhTeGRGc0xPbVRudlYrWjV4bEZDUFIrajN2UmtqTGFzeSIsIm1hYyI6ImQ2ZTRiYTY2NWNhY2I0MWY1MjFmYmNkOTU5YmZhOGU5ZGJlMWMzZDI1MGY2MzQ0NmVlNjFlMWNkN2M3NGY3NmQifQ%3D%3D',
    'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1726164218096%2Cregion:%27TR%27}',
    '_ga': 'GA1.3.1236182181.1726164223',
    '_gid': 'GA1.3.87086656.1726164223',
    '_gat': '1',
    '_ga_N0K6XSDCRJ': 'GS1.3.1726164224.1.0.1726164224.60.0.0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.exploit-db.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6Ik1xTGRaWitva1IxS2tJaW43dWdHbEE9PSIsInZhbHVlIjoiRmxUQ2twTFRHR045OXlwSTJKd3I0ZVVmTFpiTk8zd3BHanhkWjJVMG1XWkI5RGlGZDhBbkNxaHkxbGFUaEJYQyIsIm1hYyI6IjM2NzVkMjVhZjE4N2MzNDlkMWE1Y2E2OTUwZTM0MTQxY2U2MGRmYzhmNTBiODc1NDQ5OGFlZTUxNGM1MzJkMWEifQ%3D%3D; exploit_database_session=eyJpdiI6ImhYS2JhR0piUllLQmpNeHRiOG91WVE9PSIsInZhbHVlIjoibWNmbTZGYUorcWF1TFNIWmZVRXhWbXpYOHhtNVZqQnhTeGRGc0xPbVRudlYrWjV4bEZDUFIrajN2UmtqTGFzeSIsIm1hYyI6ImQ2ZTRiYTY2NWNhY2I0MWY1MjFmYmNkOTU5YmZhOGU5ZGJlMWMzZDI1MGY2MzQ0NmVlNjFlMWNkN2M3NGY3NmQifQ%3D%3D; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1726164218096%2Cregion:%27TR%27}; _ga=GA1.3.1236182181.1726164223; _gid=GA1.3.87086656.1726164223; _gat=1; _ga_N0K6XSDCRJ=GS1.3.1726164224.1.0.1726164224.60.0.0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'draw': '2',
    'columns[0][data]': 'date_published',
    'columns[0][name]': 'date_published',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'true',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': 'download',
    'columns[1][name]': 'download',
    'columns[1][searchable]': 'false',
    'columns[1][orderable]': 'false',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': 'application_md5',
    'columns[2][name]': 'application_md5',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': 'verified',
    'columns[3][name]': 'verified',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'false',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': 'description',
    'columns[4][name]': 'description',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'false',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': 'type_id',
    'columns[5][name]': 'type_id',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'false',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': 'platform_id',
    'columns[6][name]': 'platform_id',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'false',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'columns[7][data]': 'author_id',
    'columns[7][name]': 'author_id',
    'columns[7][searchable]': 'false',
    'columns[7][orderable]': 'false',
    'columns[7][search][value]': '',
    'columns[7][search][regex]': 'false',
    'columns[8][data]': 'code',
    'columns[8][name]': 'code.code',
    'columns[8][searchable]': 'true',
    'columns[8][orderable]': 'true',
    'columns[8][search][value]': '',
    'columns[8][search][regex]': 'false',
    'columns[9][data]': 'id',
    'columns[9][name]': 'id',
    'columns[9][searchable]': 'false',
    'columns[9][orderable]': 'true',
    'columns[9][search][value]': '',
    'columns[9][search][regex]': 'false',
    'order[0][column]': '9',
    'order[0][dir]': 'desc',
    'start': '0',
    'length': '15',
    'search[value]': '',
    'search[regex]': 'false',
    'author': '',
    'port': '',
    'type': '',
    'tag': '',
    'platform': '',
    '_': '1726164253167',
}

response = requests.get('https://www.exploit-db.com/', params=params, cookies=cookies, headers=headers)

#print(response.text)
jsonData = response.json()

exploits = jsonData['data']

for exploit in exploits:
	id = exploit['id']
	title = exploit['description'][1]
	type = exploit['type']['display']
	platform = exploit['platform']['platform']
	author = exploit['author']['name']
	link = "https://www.exploit-db.com"+exploit['download'].split("\"")[1]

	print(id,title,type,platform,author,link)

#print(jsonData['data'][0]['id'])