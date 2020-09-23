import requests
import time
import os

def GetMiddleText (text , head , end):
    p_start = text.find(head)
    if p_start >= 0:
        p_start = p_start + len(head)
        p_end = text.find(end,p_start)
        if p_end >= 0:
            return text[p_start:p_end].strip()
def GetImg (type):
    if (type == 1): #必应国内版
        ImgLink = "https://cn.bing.com" + GetMiddleText(requests.get("https://cn.bing.com/?FORM=BEHPTB").text , 'href="' , '"')
    elif (type == 2): #必应国际版
        ImgLink = "https://cn.bing.com" + GetMiddleText(requests.get("https://cn.bing.com/?FORM=BEHPTB&ensearch=1").text , 'href="' , '"')
    return requests.get(ImgLink).content
def SaveImg (img,path , type):
    name = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if (type == 1): #必应国内版
        name = name + "-cnbing.jpg"
    elif (type == 2): #必应国际版
        name = name + "-enbing.jpg"
    with open(file = path + name , mode = "wb") as fo:
        fo.write(img)
def main ():
    print("请选择下载的地址编号")
    print("1.必应国内版","2.必应国际版")
    type = int (input())
    print("请选择下载到的地方")
    print("1.桌面", "2.相册" , "3.自定义")
    ptype = int(input())
    if (ptype == 1): #桌面
        path = os.path.join(os.path.expanduser('~'),"Desktop") + "\\"
    elif (ptype == 2): #相册
        path = os.path.join(os.path.expanduser('~'),"Pictures") + "\\"
    elif (ptype == 3): #自定义
        path = input() + "\\"
    print("开始下载啦！")
    SaveImg(GetImg(type),path , type)
    print("已经下载完成啦")
main()