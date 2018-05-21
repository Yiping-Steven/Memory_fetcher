# coding:utf-8
import re
import time
import json
import imaplib
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header


class GetMail(object):
    @classmethod
    def mail_login(self, mail_type, mail_ssl, mail_username, mail_password):
        """邮箱登录,并检索目标人未读邮件"""
        get_server = imaplib.IMAP4_SSL(mail_type, mail_ssl)
        get_server.login(mail_username, mail_password)
        get_server.select("INBOX")  # 默认收件夹是INBOX
        typ, data = get_server.search(None, 'ALL')  # SEEN--已读邮件,UNSEEN--未读邮件,ALL--全部邮件
        #data是一个只有1元素的列表，里面存储所有邮件编号
        if data[0]:
            number_list = data[0].split()  # 处理邮件编号list,编号越大邮件时间越近
            print(number_list[-1])
            for the_mail_number in number_list:
                # 邮件内容详情
                mail_data = str(get_server.fetch(the_mail_number, '(RFC822)')[1])
                if '.png' in mail_data:
                    continue
                if '.gif' in mail_data:
                    continue
                if '.jpg' in mail_data:
                    continue
                if '._' in mail_data:
                    continue
                if '@.' in mail_data:
                    continue
                print(the_mail_number)
                tmp1 = mail_data.find('Subject:')
                print(mail_data[tmp1:tmp1+30])
                file_name='mail/'+str(int(the_mail_number))+'.html'
                with open(file_name,'w') as f:
                    f.write(mail_data)
        else:
            print( "未检索到未读邮件")

def process_start(user_id, user_pass):
    ret = GetMail.mail_login(mail_type='mails.tsinghua.edu.cn',
                             mail_ssl=993,
                             mail_username=user_id,
                             mail_password=user_pass)


if __name__ == "__main__":
    # 执行程序
    user_id=input('Please input user email address:')
    user_pass=input('Please input user password:')
    os.makedirs('mail')
    process_start(user_id, user_pass)
