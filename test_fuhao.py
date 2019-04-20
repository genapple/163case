#-*- coding:UTF-8 -*-
from selenium import webdriver
import  time
from public import  login
import read
import  unittest
class Teshu(unittest.TestCase):
    '''登录等数字符用例'''
    def setUP(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url="http://mail.163.com"
        self.verificationErrors=[]
    #用户名和密码输入特殊字符
    def tests_teshu(self):
        '''用户名和密码输入特殊字符'''
        k=read.read()
        driver=self.driver()
        driver.get(self.url)
        time.sleep(2)
        username='##2'
        ped


