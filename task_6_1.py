import requests
import json

data = []
processed_data = []
spammer = {}
response = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
content = response.text
f_name='nginx_logs.txt'
with open(f_name, 'w', encoding='utf-8') as file:
    file.write(content)
with open(f_name, 'r', encoding='utf-8') as file:
        for row in file:
            raw_row = row.split()
            rov_data = json.dumps(raw_row)
            processed_rov = json.loads(rov_data)
            processed_data = [processed_rov[0], processed_rov[5][1:], processed_rov[6]]
            data.append(processed_data)
            spammer[processed_rov[0]] = spammer.get(processed_rov[0], 0) + 1
session_counter = 0
for key in spammer:
    if spammer[key] > session_counter:
        session_counter =  spammer[key]
        spam_ip = key
print("У спамера ip адрес:  ",  spam_ip, 'Количество попыток:  ', spammer[spam_ip])
