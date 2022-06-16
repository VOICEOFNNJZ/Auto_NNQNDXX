import requests
import re

SSUUID=""#将抓包得来的cookie中的SSUUID粘贴到引号中间

headers={"Cookie":"SSUUID="+SSUUID}

def GetStudyID():#更新课程id
    url_get="http://qndxx.bestcood.com/mp/nanning/my/index.html"
    id=requests.get(url_get,headers=headers);id=re.findall(r'(detail_)(.*)(\.html)',id.text);id=re.search(r'\d+',str(id));id=id.group()
    return id

def Study():#发送post
    url_hit="http://qndxx.bestcood.com/mp/nanning/DaXueXi/LearnHit.html"
    body={"id": GetStudyID()}
    study_result = requests.post(url_hit,headers=headers,data=body)
    return study_result.text

def GetState():#只是多写了个def懒得删
    result=re.findall(r'("code":)(.*)(,"msg")',Study());result=re.search(r'\d',str(result));result=result.group()    
    if float(result) !=0:
        print("Error!")
        return
    else:
        print("Success!")
        return

GetState()
