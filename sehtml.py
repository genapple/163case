#!/usr/bin/python
#-*- coding:UTF-8 -*-
import unittest
import  HTMLTestRunner
class learn(unittest.TestCase):
    def test_1(self):
        print 'a'

    def test_2(self):
        print '2'
    def test_3(self):
        print '3'

    def test_4(self):
        print '4'
if __name__ == '__main__':
    filename="D:\untitled\sele-python\\163testcase\\163case\\rrr.html"
    fp=file(filename,'wb')
   #定义测试报告的标题和描述
    suitetest=unittest.TestSuite()
    suitetest.addTest(learn)
    #suite=unittest.makeSuite(learn)
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'woshi biaoti',description=u'ceshibaogaodemiaoshu')
    runner.run(suitetest)
    print 'lll'
    fp.close()