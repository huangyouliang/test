import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
data = {
              i:fish
              123
              from:AUTO
              to:AUTO
              smartresult:dict
              client:fanyideskweb
              salt:1501175290452
              sign:f248f45946f699b1d47d2da66c86d673
              doctype:json
              version:2.1
              keyfrom:fanyi.web
              action:FY_BY_CL1CKBUTTON
              typoResult:true
       }
response = urllib.request.urlopen(url,data)
html =  response.read().decode('utf-8')

print (html)
