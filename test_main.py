import unittest
import os
from unittest.mock import patch
from io import StringIO
from main import readTXT,filterAndCut,getVector,cosineSimilarity,compute_similarity,main
#测试各模块函数功能
class TestCheck(unittest.TestCase):
    #文件读取模块
    def test1_readTXT(self):
        with open('only_for_temp_test.txt','w') as file:
            file.write('3123004540')
        num = readTXT('only_for_temp_test.txt','测试文件')
        os.remove('only_for_temp_test.txt')
        self.assertEqual(num,'3123004540')
    def test2_readTXT(self):
        with self.assertRaises(SystemExit) as cm:
            readTXT('不会存在的路径/大顶堆/大多数','测试文件')
        self.assertEqual(cm.exception.code,'InvalidPath!')
    #文本处理模块
    def test_filterAndCut(self):
        text='今天是星期天,天气晴,今天晚上我要去看电影.triangle double test007.'
        expected=['今天','是','星期天','天气','晴','今天','晚上','我要','去','看','电影','triangle','double','test007']
        self.assertEquals(filterAndCut(text),expected)
    #向量生成模块
    def test_getvector(self):
        word1=['我','你','它','更好','我','你','更好','更好','你','我','你']
        word2=['你','更好']
        vec1,vec2=getVector(word1, word2)
        sum=0
        for i in range(len(vec1)):
            sum+=vec1[i]*vec2[i]
        self.assertEquals(sum,7)
    #余弦相似度计算模块
    def test1_cosineSimilarity(self):
        vec1=[1,2,3]
        vec2=[1,2,3]
        self.assertEquals(cosineSimilarity(vec1,vec2),1.0)
    def test2_cosineSimilarity(self):
        vec1=[0,0,0]
        vec2=[1,2,3]
        self.assertEquals(cosineSimilarity(vec1,vec2),0.0)
    def test3_cosineSimilarity(self):
        vec1=[0,0,0]
        vec2=[0,0,0]
        self.assertEquals(cosineSimilarity(vec1,vec2),1.0)
    #总体计算模块
    def test_compute_similarity(self):
        origText='今天是星期天,天气晴,今天晚上我要去看电影.triangle double test007.'
        copyText='今天是周天,天气晴朗,我晚上要去看电影.trishape float test005.'
        similarity = compute_similarity(origText,copyText)
        self.assertIsInstance(similarity,float)
        self.assertGreaterEqual(similarity,0.0)
        self.assertLessEqual(similarity,1.0)
#测试主函数
class TestMain(unittest.TestCase):
    @patch('sys.argv',['main.py','orig.txt','orig_copy.txt','ans.txt'])
    @patch('main.readTXT')
    @patch('main.compute_similarity')
    @patch('builtins.open',new_callable=unittest.mock.mock_open)
    def test_main(self,mock_open,mock_compute_similarity,mock_readTXT):
        mock_readTXT.side_effect=['原文内容','抄袭版内容']
        mock_compute_similarity.return_value=0.8888

        main()

        mock_open.assert_called_with('ans.txt','w',encoding='utf-8')
        handle=mock_open()
        handle.write.assert_called_with('相似度 : 88.88%')
