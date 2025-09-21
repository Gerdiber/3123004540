from main import readTXT,compute_similarity
path_F='FileFor10Test/'
path_B='.txt'
orig_name='原文版文件'
copy_name='抄袭版文件'
with open('result_10test.txt','w',encoding='utf-8') as f:
    for i in range(1,11,1):
        orig_path=path_F+str(i*2-1)+path_B
        copy_path=path_F+str(i*2)+path_B
        orig_content=readTXT(orig_path,orig_name)
        copy_content=readTXT(copy_path,copy_name)
        print('测试例:',i)
        print(orig_name,': ',orig_content)
        print(copy_name,': ',copy_content)
        result=compute_similarity(orig_content,copy_content)*100
        print(f'相似度: {result:.2f}%\n')
        f.write(orig_name+': '+orig_content+'\n')
        f.write(copy_name+': '+copy_content+'\n')
        f.write(f"相似度 : {result:.2f}%\n\n")
