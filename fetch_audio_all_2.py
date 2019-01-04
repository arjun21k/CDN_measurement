import csv
import urllib.request
import codecs
import json
import time

key = 'A.5d72a52bd6ec5c3b77fa03f75e85d863'
key_old = 'A.aada49748da06b441cef2a9cb402fd94'
key1 = 'A.735aed4f374531925e8e493c4cbb05c9'
key2 = 'A.7fc1644f7b6e1b73a67018f6c6849677'
key3 = 'A.8ceec3ca4f9be05d5a2c9c72f034dcde'
key4 = 'A.af1532e21d632aa5e1fa8f33dc41a084'
# url = 'https://yahoo.com'
# script='setDns%20www.yahoo.com%2072.30.35.9%0Anavigate%20www.yahoo.com'
# script1='setDns www.yahoo.com 72.30.35.9\nnavigate www.yahoo.com'
# script2 = parse.quote_plus(script1)

suffixListEurope = ['London', 'Italy', 'Stockholm2', 'Prague', 'Maidenhead', 'Berlin', 'Strasburg_FR', 'Falkenstein',
                    'gce-europe-west1-linux', 'Amsterdam', 'Poland', 'Spain']

# 'Dulles:Chrome.DSL' to be included in the below list
suffixListAmerica = ['SanFrancisco', 'Texas2', 'ec2-us-west-1', 'NewJersey', 'Toronto:Chrome.DSL', 'Argentina2', 'ec2-us-east-1', 'Florida',
                     'ec2-sa-east-1', 'Chicago:Chrome.DSL', 'Nebraska', 'MinasGerais_BR', 'gce-us-west1-linux', 'Argentina', 'Colorado']
temp = ['ec2-us-east-1']

for loc in temp:

    print("Location: " + loc)
    ofileName = loc.replace(":", "")
    ofileName = ofileName.replace(".", "")
    writeCSV = open(ofileName + ".csv ", "w", encoding='utf=8')
    writeCSV.write("IP,ttfb_ms,ping_ms\n")

    #europeIPs = ['8.252.29.244', '67.24.143.244', '8.252.8.244', '8.253.140.106', '8.250.103.245',
    #            '67.24.139.244', '8.250.87.248', '8.253.157.244', '8.250.89.243', '8.253.156.110']

    americasIps = ['67.26.241.244', '8.27.231.244', '67.24.197.248', '8.253.129.177', '8.250.99.243', '8.252.103.116', '8.252.16.244',
                   '8.249.225.243', '8.253.165.238', '8.252.10.116', '8.253.197.45', '8.252.85.116', '8.253.133.238', '8.252.88.116', '8.253.148.236']


    for ip in americasIps:
        script_hulu_audio = "setDns%20http-v-darwin.hulustream.com%20" + ip + "%0Anavigate%20https%3A%2F%2Fhttp-v-darwin.hulustream.com%2F885%2F60830885%2Fagave51042130_52966074_H264_1000_52966608_audio.mp4%3Fend%3D20181208015204%26authToken%3D03051e2db7f9322708b67"
        url = 'http://www.webpagetest.org/runtest.php?&location=' + loc + '&script=' + script_hulu_audio + '&f=json&k=' + key4

        # url1 = "http://www.webpagetest.org/runtest.php?script=" + script2 + "&f=json&k=" + key
        jsonres = urllib.request.urlopen(url)
        res_body = jsonres.read()
        # # This json response holds the location of link (inside data.detailsCSV) where results are there.
        jsonresponse = json.loads(res_body.decode("utf-8"))
        print(jsonresponse)
        url2 = str(jsonresponse["data"]["detailCSV"])
        testId = str(jsonresponse["data"]["testId"])
        #print(url2)
        #print(testId)

        # Check whether the test results are available
        while (1):
            url3 = "http://www.webpagetest.org/testStatus.php?f=json&test=" + testId
            jsonres1 = urllib.request.urlopen(url3)
            res_body1 = jsonres1.read()
            jsonresponse1 = json.loads(res_body1.decode("utf-8"))
            print(jsonresponse1)
            testStatus = str(jsonresponse1["statusCode"])
            if testStatus == "200":
                break
            time.sleep(30)

        ftpstream = urllib.request.urlopen(url2)
        csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
        count = 0

        for row in csvfile:
            if (count == 0):
                for col in range(len(row)):
                    if row[col] == 'ip_addr':
                        index_ip_addr = col
                    if row[col] == 'cdn_provider':  # host
                        index_cdn = col
                    if row[col] == 'ttfb_ms':  # host
                        index_ttfb = col
                    if row[col] == 'server_rtt':  # host
                        index_ping = col
                    count = 1
                continue

            cdn = row[index_cdn]
            ip = row[index_ip_addr]
            ttfb = row[index_ttfb]
            ping = row[index_ping]

            print(" IP: " + ip + " ttfb: " + ttfb + " Ping: " + ping)
            writeCSV.write(ip + ',' + ttfb + ',' + ping + '\n')
            break
    writeCSV.close()
