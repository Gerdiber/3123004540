import re
import jieba
#过滤标点符号并使用jieba分词
def filterAndCut(content):
    pattern=r'([a-zA-Z0-9]+|[\u4e00-\u9fa5]+)'
    segments=re.findall(pattern,content)
    cutText=[]
    for segment in segments:
        if re.match(r'[\u4e00-\u9fa5]+',segment):
            cutText.extend(jieba.lcut(segment))
        else:
            cutText.append(segment.lower())
    return cutText