import requests
import os
def changeWeb(url): 

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
    response = requests.get(url, headers=headers)

    # if previous.txt doesn't exist yet, open empty file for writing 
    if not os.path.exists("previous.html"):
        open("previous.html", 'w+', encoding="utf-8").close()

    f = open("previous.html", 'r', encoding="utf-8")
    previous = f.read() 
    f.close()

    if response.text == previous:
        return print('No updates.')
    else:
        f = open("previous.html", 'w', encoding="utf-8")
        f.write(response.text)
        f.close()
        return print('Update available!')

url = "http://www.eroakirkosta.fi/" #url to monitor
changeWeb(url)