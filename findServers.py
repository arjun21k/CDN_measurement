import fetch_api
import time
import threading
url_list = ['https://www.hulu.com/watch/88e8641f-b757-42e0-a007-33a4228eb94d']
# 'https://www.hulu.com/watch/f5602d72-72b6-4ad8-918a-714726e70221']
# 'https://www.hulu.com/search']
# 'https://www.hulu.com/movie/sub-akira-64a5a8d0-1406-4178-97a5-2649504faa85']
# 'https://www.hulu.com/watch/f3b8c70c-2bf9-4ab7-9a51-89abd06fca61'] #unpopular
    # 'https://www.hulu.com/watch/136a40eb-8085-4dae-80df-3a8c2d784441']
    # 'https://www.hulu.com/']
    # 'https://www.hulu.com/watch/05e869d6-5a84-40c3-9c97-720c3a32d40a',
    # 'https://www.hulu.com/series/this-is-us-9dc170da-85db-475d-9df4-6572f15ffb00']
#     ,
#     'https://www.hulu.com/watch/0f7ed39a-0df8-415d-8c11-286caebdc8f9',
#     'https://www.hulu.com/watch/b2cda97f-c8bf-4ef1-8f00-92432a87870c',
#     'https://www.hulu.com/watch/5684da0d-fb27-4a11-b636-d1fe73bb2149'
#
# ]

suffix_list = ['Dulles:Chrome.DSL', 'Clifton:Chrome.DSL', 'NewYork:Chrome.DSL',
               'Orlando:Chrome.DSL', 'Chicago:Chrome.DSL', 'Lincoln:Chrome.DSL', 'Denver:Chrome.DSL',
                'Phoenix:Chrome.DSL', 'California:Chrome.DSL', 'LosAngeles:Chrome.DSL', 'Oregon:Chrome.DSL',
                'Toronto:Chrome.DSL', 'Virginia:Chrome.DSL']
# index = 0
master_list = []
key = 'Akamai'
for suffix in suffix_list:
    csv_files = []
    for url in url_list:
        url1 = "http://www.webpagetest.org/runtest.php?url="+url+"&f=json&k=A.aada49748da06b441cef2a9cb402fd94&"+suffix
                                                                 # "aada49748da06b441cef2a9cb402fd94"
                                                                 # "d5b031de8c776a15316d5e40768985fd&"+suffix
        # 735aed4f374531925e8e493c4cbb05c9
        # file = threading.Thread(target=fetch_api.get_csv, args=(url1))
        file = fetch_api.get_csv(url1)
        csv_files.append(file)
        print (file)
        # time.sleep(10)

        # index += 1
time.sleep(120)
    # print (csv_files)
    # print (fetch_api.decode_results(csv_files))
temp_list = (fetch_api.decode_results(csv_files))
print (temp_list)
if temp_list.has_key('Akamai'):
    for item in temp_list['Akamai']:
        master_list.append(item)
#
print(master_list)
