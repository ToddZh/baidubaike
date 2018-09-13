import requests

url = 'https://baike.baidu.com/'
print("downloading with requests")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Content-Encoding': 'deflate'}
r = requests.get(url,headers=headers,timeout=10)
with open("./new/test", "wb") as code:
	code.write(r.content)