import csv
from urllib3 import request
import urllib
import codecs
import pandas as pd
import json
import time


url2 = "http://www.webpagetest.org/runtest.php?url=www.google.com&f=json&k=A.aada49748da06b441cef2a9cb402fd94"
url1 = "http://www.webpagetest.org/runtest.php?url=https://www.hulu.com/watch/05e869d6-5a84-40c3-9c97-720c3a32d40a&f=json&k=A.aada49748da06b441cef2a9cb402fd94"
jsonres = urllib.urlopen(url1)
res_body = jsonres.read()
# res_body = json.load(jsonres)
# print(res_body)
jsonresponse = json.loads(res_body.decode("utf-8"))
print(jsonresponse)
url2 = str(jsonresponse["data"]["detailCSV"])
print(url2)
time.sleep(60)

ftpstream = urllib.urlopen("https://www.webpagetest.org/result/181107_J4_1a99f18b84ebe2e529d4b9196b08138b/requests.csv")
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
i = 0
cdn_servers = {}
for row in csvfile:
    for col in range(len(row)):
        if row[col] == 'ip_addr':
            index_ip_addr = col
        if row[col] == 'cdn_provider':
            index_cdn = col;
    break;

for row in csvfile:
    cdn = row[index_cdn]
    ip = row[index_ip_addr]
    print ("cdn "+cdn)
    if (cdn == '' or ip == ''): continue
    if(cdn_servers.has_key(cdn)):
        cdn_servers[cdn].append(ip)
    else:
        cdn_servers[cdn] = []
        cdn_servers[cdn].append(ip)
# df = pd.read_csv(ftpstream)
# print(df.head(2))

print (cdn_servers)
