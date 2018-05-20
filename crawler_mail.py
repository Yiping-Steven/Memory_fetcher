# coding:utf-8
import re
import time
import json
import imaplib
import smtplib
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
                file_name=str(int(the_mail_number))+'.html'
                with open(file_name,'w') as f:
                    f.write(mail_data)
        else:
            print( "未检索到未读邮件")

    # @classmethod
    # def send_mail(self, mail_type, mail_username, mail_password):
    #     """发送邮件"""
    #     # 邮件内容
    #     msg = self.the_task()       # 获取文件数据内容
    #     message = MIMEText("'%s'" % msg, 'plain', 'utf-8')
    #     # 发件人
    #     message['From'] = Header(mail_username, 'utf-8')
    #     # 收件人
    #     message['To'] = Header(the_pattern, 'utf-8')
    #     # 邮件主题
    #     message['Subject'] = Header('邮件主题:测试', 'utf-8')
    #     # 发件服务器
    #     send_mail_type = 'smtp.exmail.qq.com'
    #     try:
    #         # 发短信采用默认端口25,不然会报错
    #         send_server = smtplib.SMTP(send_mail_type, 25)
    #         send_server.login(mail_username, mail_password)
    #         send_server.sendmail(mail_username, the_pattern, message.as_string())
    #         print( "邮件发送成功!!!")
    #         send_server.quit()
    #     except smtplib.SMTPException:
    #         print( "邮件发送失败")


def process_start():
    ret = GetMail.mail_login(mail_type='mails.tsinghua.edu.cn',
                             mail_ssl=993,
                             mail_username='',
                             mail_password='')


if __name__ == "__main__":
    # 执行程序
    process_start()
