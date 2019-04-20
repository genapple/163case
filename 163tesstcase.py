#!/usr/bin/python
#-*- coding:UTF-8 -*-
import unittest
import  test_login
from HTMLTestRunner import HTMLTestRunner
import  time
import os
import smtplib
from email.mime.text import MiMeMultipart
from email.header import Header
def new_file():
    lists=os.listdir(test_report_dir)
    lists.sort(key=lambda fn:os.path.getmtime(test_report_dir+'\\'+fn))
    file_path=os.path.join(test_report_dir,lists[-1])
    return file_path
def send_email():
    f=open(new_file(),'rb')
    mail_body=f.read()
    f.close()
    smtpserver='smtp.163.com'
    user='XXXX@163.com'
    password='XXXX'
    sender='XXXX@163.com'
    receiver='XXX@qq.com'
    subject="一封自动发送163邮箱测试报告"
    msg=MiMeMultipart('mixed')
    att=MIMEText(mail_body,'html','utf-8')
    att['Content-type']='application/octest-stream'
    att['Content-Disposition']='attachment';filename='results.html'
    msg.attach(att)
    msg['From']='XXX@163.com'
    msg['To']='XXXX#163.com'
    msg['Subject']=Header(subject,'utf-8')

    smtp=smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
if __name__ == '__main__':
    test_dir="D:\\untitled\\sele-python\\.idea"
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now=time.strftime("%Y-%M-%R %H_%M_%S")
    test_report_dir="D:\\untitled\\sele-python\\.idea"
    filename=test_report_dir+"\\"+now+'result.html'
    fv=open(filename,'wb')
    runner=HTMLTEstRunner(stream=fv,title='163邮箱登录测试报告',description='用例执行情况')
    runner.run(discover)
    fv.close()
    send_email()










