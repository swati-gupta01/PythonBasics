import requests
import time

urls=('https://facebook.com','https://oreilly.com','https://twitter.com')
t1=time.time()
for resp in( requests.get(url) for url in urls):
    print(len(resp.content),'->',(resp.status_code),'_>',resp.url)
t2=time.time()
print('time:',str(t2-t1))