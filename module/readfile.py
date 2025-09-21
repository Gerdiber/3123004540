import os
#以utf-8读取txt文本
def readTXT(file_path,filename):
    if not os.path.exists(file_path):
        print(filename+"路径无效")
        exit('InvalidPath!')
    with open(file_path,'r',encoding='utf-8') as f:
        content=f.read()
    return content