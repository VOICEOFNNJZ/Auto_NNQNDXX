import requests
import re
import json

# 将抓包得来的cookie中的SSUUID粘贴到引号中间
SSUUID = ""

# 以下内容无需更改

headers = {
	"Cookie": "SSUUID=" + SSUUID,
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/tpg,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; MI MIX 4 Build/S2.MBRJUN.0523; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20211202 Mobile Safari/537.36 MMWEBID/4381 MicroMessenger/8.0.18.2062(0x28001241) Process/toolsmp WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_TW ABI/arm64 "
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
