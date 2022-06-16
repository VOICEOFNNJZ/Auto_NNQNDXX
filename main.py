import requests
import re
import json

# 将抓包得来的cookie中的SSUUID粘贴到引号中间
SSUUID = ""

# 以下内容无需更改

headers = {
	"Cookie": "SSUUID=" + SSUUID
}

def GetStudyID(): # 得到课程id
	url_get = "http://qndxx.bestcood.com/mp/nanning/my/index.html"
	response = requests.get(url_get, headers = headers)
	if ('<title>抱歉，出错了</title><meta charset="utf-8">' in response.text):
		return -1
	id = re.findall(r'(?<=\/mp\/nanning\/daxuexi\/detail_)\d+(?=\.html)', response.text)
	return id[0]

def Study(): # 发送post
	url_hit = "http://qndxx.bestcood.com/mp/nanning/DaXueXi/LearnHit.html"
	id = GetStudyID()
	if (id == -1): 
		return -1
	data = {"id": id}
	response = requests.post(url_hit, headers = headers, data = data)
	return int(json.loads(response.text)['code'])

code = Study()
if (code != 0):
	print("Error!")
else:
	print("Success!")
