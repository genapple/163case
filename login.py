#!/usr/bin/python
#-*- coding:UTF-8 -*-
from selenium import  webdriver
driver=webdriver.Chrome()
driver.get("https://mail.163.com/")
email=driver.find_elements_by_name("email")
email.send_keys("13917408993")
password=driver.find_element_by_name("password")
password.send_keys("yss135792")
