import urllib
import json
import csv
import codecs


def get_csv(url):
    jsonres = urllib.urlopen(url)
    res_body = jsonres.read()
    jsonresponse = json.loads(res_body.decode("utf-8"))
    print(jsonresponse)
    try:
        csvfile = str(jsonresponse["data"]["detailCSV"])
        # print ("here")
        return csvfile
    except:
        return None
    # time.sleep(60)

def decode_results(files):
    master_cdn_dict = {}
    for file in files:
        if file == None: continue
        ftpstream = urllib.urlopen(file)
        csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
        cdn_servers = {}
        for row in csvfile:
            for col in range(len(row)):
                if row[col] == 'ip_addr':
                    index_ip_addr = col
                if row[col] == 'cdn_provider':
                    index_cdn = col
            break

        for row in csvfile:
            cdn = row[index_cdn]
            ip = row[index_ip_addr]
            # print ("cdn " + cdn)
            if (cdn == '' or ip == ''): continue
            if (master_cdn_dict.has_key(cdn) ):
                # print (ip)
                if(ip not in master_cdn_dict[cdn]):
                    master_cdn_dict[cdn].append(ip)
            else:
                master_cdn_dict[cdn] = []
                master_cdn_dict[cdn].append(ip)

        print (master_cdn_dict)

    return (master_cdn_dict)