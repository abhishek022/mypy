import urllib.request
import re
import urllib.parse

#x=urllib.request.urlopen('https://www.google.com')
#print(x.read())

url="https://www.pythonprogramming.net/"
values={'s':'basic','submit':'search'}
data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respdata=resp.read()


para=re.findall(r'<p>(.*?)</p>',str(respdata))
for word in para:
    print(word)

