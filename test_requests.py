import io
from datetime import datetime
import csv
import time
t = time.time()
count = 0
blocked_count = 0
import speedtest
import requests
# detect = """<img src="mdes.jpg" width="800" height="700">"""
detect = f'<img src="mdes.jpg'
fb = f"When this happens, it's usually because the owner only shared it with         a small group of people or changed who can see it, or it's been deleted."
date = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year} {datetime.now().strftime("%X")}'
print(date)
# speedtest
# s = speedtest.Speedtest()
# print(f'My download speed is: {s.download()/10**6} Mbps', )
# print(f'My upload speed is: {s.upload()/10**6} Mbps')
# best_server = s.get_best_server()
# for key, value in best_server.items():
#     print(key, ' : ', value)

with open('Blocked_Check.csv', "r", encoding='utf-8') as infile:
    reader = csv.reader(infile)
    next(reader)
    for line in reader:
        url = line[0]
        if url == "":
            continue
        # print(url)
        count += 1
        if line[1] == 'FB':
            if requests.get(url, verify=False).text.find(fb) + 1 != False:
                print(f'{url.replace("https://", "").replace("www.", "")} was blocked @{datetime.now().strftime("%X")}')
                blocked_count += 1
            else:
                pass
            continue
        if requests.get(url, verify=False).text.find(detect) + 1 != False:
            print(f'{url.replace("https://", "").replace("www.", "").replace("/", "")} was blocked by MDES @{datetime.now().strftime("%X")}')
            blocked_count += 1
        else: pass
        time.sleep(0.1)
print(f'{count} Urls Checked')
print(f'Runtime : {round(time.time()-t,2)} seconds')