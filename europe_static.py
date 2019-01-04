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
key5 = 'A.6394bf1e9ee6170c6073c68f20d6dff2'
key6 = 'A.6a18386c8e76c2d92162ddcc21a9a847'
key7 = 'A.D5b031de8c776a15316d5e40768985fd' # INVALID
key8 = 'A.144b7445e77e95c65b54b2a1ed828867'

suffixListEurope = ['Italy', 'Stockholm2', 'Maidenhead', 'Berlin', 'Falkenstein',
                    'Poland', 'Spain', 'gce-europe-west1-linux', 'Amsterdam', 'London', 'Prague']

temp = ['London']

for loc in temp:

    print("Location: " + loc)
    ofileName = loc.replace(":", "")
    ofileName = ofileName.replace(".", "")
    writeCSV = open("./eu_static_force_resolve_3/" + ofileName + ".csv ", "w", encoding='utf=8')
    writeCSV.write("IP,ttfb_ms,ping_ms\n")

    euAkamaiIPs = ['23.216.206.221', '2.23.131.158', '104.103.109.11', '23.214.189.19', '104.86.40.25', '104.111.244.87',
                   '69.192.70.38', '104.81.97.152', '104.126.95.88', '104.83.156.69', '95.100.120.233']

    for ip in euAkamaiIPs:
        #script = "setDOMElement%09name%3Dshreeshrita93%40gmail.com%0Anavigate%09https%3A%2F%2Fauth.hulu.com%2Fweb%2Flogin%3Fnext%3Dhttps%253A%252F%252Fwww.hulu.com%252F%0AsetValue%09name%3Dshreeshrita93%40gmail.com%0AsetValue%09name%3Dwisconsin_acncdn%0AsetDOMElement%09className%3Dmore_pics%0AsubmitForm%09name%3DHuluLoginForm%0AsetDns%20www.hulu.com" + ip + "%0Anavigate%20https%3A%2F%2Fwww.hulu.com%2F"
        #script_hulu_audio = "setDns%20www.hulu.com%20" + ip + "%0Anavigate%20https%3A%2F%2Fhttp-v-darwin.hulustream.com%2F885%2F60830885%2Fagave51042130_52966074_H264_1000_52966608_audio.mp4%3Fend%3D20181208015204%26authToken%3D03051e2db7f9322708b67"
        script = "setDns%20www.hulu.com%20" + ip + "%0Anavigate%20https%3A%2F%2Fwww.hulu.com%2Fstatic%2Fhitch%2F_next%2Ff8f8d4f16424e7d092e5122292d9036b803d9f62%2Fpage%2FLandingPage.js"
        url = 'http://www.webpagetest.org/runtest.php?&location=' + loc + '&script=' + script + '&f=json&k=' + key1

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
            #print(row)
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
