# -*- coding = UTF-8 -*-
import os

def jm1(str , p): #加密主函数
    i = 0 #给i赋初值0
    str = list(str)
    res = str #将str赋值给res，让res为相同位数的列表
    while i < len(str):
        if (res[i] != '\n'):
            if (ord(str[i]) + p <= 127):  # 当偏移后的字母未超出ASCII范围
                res[i] = chr(ord(str[i]) + p)  # 将数据进行偏移加密处理
            else:
                res[i] = chr(ord(str[i]) + p - 127) #越界从头开始
        i=i+1 #下标往后移动一格
    return "".join(res) #将结果转化成字符串输出

def jm2(str , p): #解密主函数
    i = 0 #给i赋初值0
    str = list (str)
    res = str #将str赋值给res，让res为相同位数的列表
    while i < len(str):
        if (res[i] != '\n'):
            if (ord(str[i]) - p >= 0):  # 当偏移后的字母未超出ASCII范围
                res[i] = chr(ord(str[i]) - p)  # 将数据进行偏移加密处理
            else:
                res[i] = chr(ord(str[i]) - p + 127) #越界从头开始
        i=i+1 #下标往后移动一格
    return "".join(res) #将结果转化成字符串输出

def main():
    fo = open("data.in","r") #读取输入的数据
    str = fo.read()
    fo.close()
    p = input("请输入偏移量：")  # 输入偏移量
    p = int(p)  # 将偏移量转为整数类型
    type = int(input("请输入加密还是解密（1.加密 ， 2.解密）:")) #输入是加密还是解密
    if p == 0:
        p = 3  # 赋予初值
    if type == 1: #加密
        fo = open("data.out", "w")
        fo.write(jm1(str, p))  # 输出结果
        fo.close()
    elif type == 2: #解密
        fo = open("data.out", "w")
        fo.write(jm2(str, p))  # 输出结果
        fo.close()

if __name__ == '__main__':
    main()