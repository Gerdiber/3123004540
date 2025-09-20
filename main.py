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

#获取原文与修改文的词频向量
def getVector(origCText,copyCText):
    #总词汇
    allword = set(origCText) | set(copyCText)
    #原文词频向量vec1
    vec1 = [0] * len(allword)
    #修改文词频向量vec2
    vec2 = [0] * len(allword)
    #分词与下标配对
    word_index={word:i for i,word in enumerate(allword)}
    #计算两分词的各词出现次数
    for word in origCText:
        index=word_index.get(word)
        if index is not None:
            vec1[index]+=1
    for word in copyCText:
        index = word_index.get(word)
        if index is not None:
            vec2[index] += 1
    return vec1,vec2


print(filterAndCut(readTXT("orig.txt")))