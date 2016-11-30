import urllib.request
#response=urllib.request.urlopen('http://www.fishc.com')
#html=response.read()
#html=html.decode('utf-8')
#print(html)



url='http://120.77.65.142:11011/TransfServices/appservice/user/cmp_uinfo.do?'
user = "18813866764"
passwd = "stt123"

response = urllib.request.urlopen(url+"key="+user+"&password="+passwd)

html=response.read()
html=html.decode('utf-8')
print(html)
