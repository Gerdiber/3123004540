import sys
from module.readfile import readTXT
from module.processText import filterAndCut
from module.computeSimilarity import getVector,cosineSimilarity

def compute_similarity(origText,copyText):
    origWord=filterAndCut(origText)
    copyWord=filterAndCut(copyText)
    vec1,vec2=getVector(origWord,copyWord)
    result=cosineSimilarity(vec1, vec2)
    return result

def main():
    if(len(sys.argv)!=4):
        print('参数过少或过多 , 请按照: python main.py [原文文件] [抄袭版文件] [答案文件] 进行输入')
        exit()
    origPath = sys.argv[1]
    copyPath = sys.argv[2]
    resultPath = sys.argv[3]
    result=compute_similarity(readTXT(origPath,'原文文件'),
                              readTXT(copyPath,'抄袭版文件'))*100
    with open(resultPath,'w',encoding='utf-8') as f:
        f.write(f"相似度 : {result:.2f}%")

if __name__ == '__main__':
    main()