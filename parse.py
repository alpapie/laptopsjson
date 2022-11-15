import json
import requests

# f=open('laptop.json','r')
# # donne=f.read()
# data=json.loads(f)
# print(data)
# f.close()

# with open('./laptop.json', encoding="utf8") as f:
#     datas = json.load(f)
#     for data in datas:
#         for laptops in data['results']:
#             for laptop in laptops['hits']:
#                 with open('datalaptopsclean.json', 'a') as json_file:
#                     laptop['_highlightResult']=None
#                     pp=json.dumps(laptop)
#                     json_file.write(pp+"\n ,")

url="https://laptopmedia.com"
headers = {
    'authority': 'laptopmedia.com',
    "path": "/laptop-specs/hp-probook-450-g6-471/",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "_ga=GA1.2.1340383237.1668434335; _gid=GA1.2.623981035.1668434335",
    "if-modified-since": "Mon, 14 Nov 2022 13:59:39 GMT",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Sidekick\";v=\"104\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.30.349.210 Safari/537.36"
           }
data=requests.get(url=url,headers=headers)
print(data.ok)
