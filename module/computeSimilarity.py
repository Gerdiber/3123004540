import math
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
    if b1==0 and b2==0:
        return 1.0
    if b1==0 or b2==0:
        return 0.0
    return a/(math.sqrt(b1)*math.sqrt(b2))