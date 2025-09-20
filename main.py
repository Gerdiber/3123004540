import sys
import re
import math
import jieba

#以utf-8读取txt文本
def readTXT(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        content=f.read()
    return content

#过滤非中文字符和标点符号并使用jieba分词
def filterAndCut(content):
    filterdText = re.sub(r'[^\u4e00-\u9fa5]','',content)
    cutText = jieba.lcut(filterdText)
    return cutText

print(filterAndCut(readTXT("orig.txt")))
