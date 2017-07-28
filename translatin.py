import urllib.request
import urllib.parse
import json
#content = input("请输入要翻译的内容:")
url= 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
data  = {}
data['from'] = 'AUTO'
data['i'] = 'fish'
data['to'] =  'AUTO'
data['smartresult'] =  'dict'
data['client'] =  'fanyideskweb'
data['salt'] =  '1501172123433'
data['sign'] =  'ef8bd3a2493fb60d797a11f507e2431a'
data['action'] =  'FY_BY_CL1CKBUTTON'
data['to'] =  'AUTO'
data['doctype'] = 'json'
data['xmlVersion'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
#print(html)
target=json.loads(html)
print('jieguo:',target)
#print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
