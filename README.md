### 作业信息:

| 这个作业属于哪个课程 | https://edu.cnblogs.com/campus/gdgy/Class34Grade23ComputerScience |
| :------------------: | :----------------------------------------------------------: |
|  这个作业要求在哪里  | https://edu.cnblogs.com/campus/gdgy/Class34Grade23ComputerScience/homework/13477 |
|    这个作业的目标    |       实现一个论文查重算法 , 学习git管理 , 学习PSP表格       |

**作业GitHub链接:** https://github.com/Gerdiber/3123004540

### PSP表格:

| PSP2.1                                  |    Personal Software Process Stages     | 预估耗时（分钟） | 实际耗时（分钟） |
| :-------------------------------------- | :-------------------------------------: | :--------------: | :--------------: |
| **Planning**                            |                  计划                   |        10        |        10        |
| · Estimate                              |       · 估计这个任务需要多少时间        |        10        |        10        |
| **Development**                         |                  开发                   |       285        |       245        |
| · Analysis                              |       · 需求分析 (包括学习新技术)       |        90        |        75        |
| · Design Spec                           |             · 生成设计文档              |        10        |        8         |
| · Design Review                         |               · 设计复审                |        10        |        5         |
| · Coding Standard                       | · 代码规范 (为目前的开发制定合适的规范) |        10        |        10        |
| · Design                                |               · 具体设计                |        25        |        20        |
| · Coding                                |               · 具体编码                |        60        |        56        |
| · Code Review                           |               · 代码复审                |        30        |        21        |
| · Test                                  | · 测试（自我测试，修改代码，提交修改）  |        50        |        50        |
| **Reporting**                           |                  报告                   |        90        |        68        |
| · Test Report                           |               · 测试报告                |        30        |        25        |
| · Size Measurement                      |              · 计算工作量               |        30        |        13        |
| · Postmortem & Process Improvement Plan |     · 事后总结, 并提出过程改进计划      |        30        |        30        |
|                                         |                 · 合计                  |       385        |       323        |

### 计算模块设计与实现过程:

#### 计算模块设计:

整体算法程序可分为：**文件文本读取模块**，**文本处理模块**，**词频向量化模块**，**余弦相似度计算模块**

**文件文本读取模块:** 接收传入的文件路径字符串，先进行验证文件是否存在可正常读取，若可以则再将文件文本以 UTF-8 编码格式读取出来以字符串形式暂存．

**文本处理模块:** 接收两个传入的字符串，分别为原文文本以及抄袭版文本．本模块将会先通过正则表达式对这些字符串进行筛选，过滤掉所有的标点符号并分离中英文词段：中文段将使用 Jieba 分词库进行分词，分词后的中文词将加入词汇；英文词则直接添加进词汇中．最后将返回两个文本各自的词汇．

**词频向量化模块:** 接收传入的两个词汇，先合并出一个总词汇，再分别计算两词汇相对于总词汇的各词出现频率，以计算出两个文本各自的词频，计算出来的两个词频向量作为结果输出．

**余弦相似度计算模块:** 接收传入的两个词频向量,根据余弦计算公式：
$$
cosθ=(A*B)/(|A|*|B|)
$$
A与B越接近，cosθ的值越接近1，反之越接近0．本模块将先计算两个词频向量的点乘积得 A * B ，再分别计算两个词频向量的模长 |A| 和 |B| ，便可计算出 cosθ ，即为两个文本的词频向量的余弦相似度．

模块整体流程图:

<img width="1178" height="278" alt="ScreenShot_2025-09-21_16-56-04" src="https://github.com/user-attachments/assets/8701dea0-2f19-41cc-ac64-29cffb6e16d9" />

#### 算法关键:

**1.文本处理：**文本无用标点符号的过滤以及英文单词数字的提取

**2.文本数据转为数学数据：**计算词频作多重维度的向量

**3.余弦相似度：**计算向量在空间中的贴合程度（计算向量的余弦值）

#### 独到之处:

1.文本处理直接过滤标点符号防止无意义符号进入词汇干扰相似度计算

2.对文件的可访问性作验证才进行读取，保证安全有效地读取文件

### 计算模块接口部分性能改进:

#### 改进耗时：

改进文本过滤处理及分词：20min

改进特殊文本余弦相似度计算：7min

#### 改进思路：

1.先进行通过正则表达式的文本过滤,将过滤出来的文本交由分词器处理,减少分词器负担加快效率

2.根据向量可能出现的特殊情况直接给出余弦相似度结果省去不必要的计算

改进后性能分析图:

<img width="1883" height="1213" alt="ScreenShot_2025-09-21_19-18-32" src="https://github.com/user-attachments/assets/02660592-fa5c-4761-91b2-78ecce92cd06" />

可以看出,耗时最多的是compute_similarity中的filterAndCut函数

### 计算模块部分单元测试:

#### 单元测试代码：

```python
import unittest
import os
from unittest.mock import patch
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

```

#### 测试的函数：

模块部分：**readTXT**，**filterAndCut**，**getVector**，**cosineSimilarity**，**compute_similarity**

主函数：**main**

#### 构造测试思路：

**1.readTXT：**分别测试正常可读取的文件路径(临时创建新文件进行读取,读取完后自动删除)以及内定正常情况无法读取到的文件路径，根据异常退出的信息或正常读取的内容判断测试是否成功

**2.filterAndCut：**给出一段设定好的文本字符串测试分词完毕后的结果是否与预期相等

**3.getVector：**给出两个词汇计算对应词频向量并计算向量点乘积是否等同预期值

**4.cosineSimilarity：**给出几组特殊向量检测结果是否等同预期值

**5.compute_similarity：**给出一组设定好的文本字符串走完相似度计算流程测试结果是否为浮点型且在范围内

**6.main：**对 Jieba 分词计算相似度结果进行模拟，测试是否能正常输出

#### 测试覆盖率截图:

<img width="913" height="442" alt="ScreenShot_2025-09-21_15-37-50" src="https://github.com/user-attachments/assets/2ad3c023-71b5-4bb8-9cb9-78e4eda3856d" />

### 计算模块部分异常处理说明:

#### 1.文件读取异常处理

设计目标:处理文件不能正常读取的情况

对应场景:文件路径有误导致文件读取异常

单元测试样例:

```python
    def test2_readTXT(self):
        with self.assertRaises(SystemExit) as cm:
            readTXT('不会存在的路径/大顶堆/大多数','测试文件')
        self.assertEqual(cm.exception.code,'InvalidPath!')
```

#### 2.文本内容异常处理

设计目标:当文本内容比较特殊时直接得到对应相似度

对应场景:文本内容为空或纯标点符号字符组成的内容

单元测试样例:

```python
    def test2_cosineSimilarity(self):
        vec1=[0,0,0]
        vec2=[1,2,3]
        self.assertEquals(cosineSimilarity(vec1,vec2),0.0)
    def test3_cosineSimilarity(self):
        vec1=[0,0,0]
        vec2=[0,0,0]
        self.assertEquals(cosineSimilarity(vec1,vec2),1.0)
```

