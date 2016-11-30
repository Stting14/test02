import urllib.request
import urllib.parse
import json


#content=input('请输入需要翻译的内容：')

#response=urllib.request.urlopen('http://placekitten.com/g/500/600')
#req=urllib.request.Request('http://placekitten.com/g/500/600')
#response=urllib.request.urlopen(req)

#cat_img=response.read()

#with open('cat_img_500_600.jpg','wb') as f:
#    f.write(cat_img)

#response.geturl()
#response.info()
#print(response.info())

#response.getcode()
while True:
    content=input('请输入需要翻译的内容(输入"q!"退出程序)：')
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'

    data={}
    data['type']='AUTO'
    data['i']=content
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'

    data=urllib.parse.urlencode(data).encode('utf-8')
    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')

    target=json.loads(html)
    print(html)
   



