import re
import math
import jieba
import sys
import os

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

#计算余弦相似度: (b1*b2)/[sqrt(b1^2)*sqrt(b2^2)]
def cosineSimilarity(vec1,vec2):
    a=0;b1=0;b2=0
    for i in range(len(vec1)):
        a+=vec1[i]*vec2[i]
        b1+=vec1[i]*vec1[i]
        b2+=vec2[i]*vec2[i]
    #避免除数为0
    if b1==0 or b2==0:
        return 0.0
    return a/(math.sqrt(b1)*math.sqrt(b2))*100

def main():
    if(len(sys.argv)!=4):
        print('参数过少或过多 , 请按照: python main.py [原文文件] [抄袭版文件] [答案文件] 进行输入')
        exit()
    origPath = sys.argv[1]
    copyPath = sys.argv[2]
    if not os.path.exists(origPath):
        print("原文文件路径无效")
        exit()
    if not os.path.exists(copyPath):
        print("抄袭版文件路径无效")
        exit()
    resultPath = sys.argv[3]
    vec1,vec2=getVector(filterAndCut(readTXT(origPath)),filterAndCut(readTXT(copyPath)))
    with open(resultPath,'w',encoding='utf-8') as f:
        f.write(f"相似度 : {cosineSimilarity(vec1,vec2):.2f}")

if __name__ == '__main__':
    main()