# coding:utf-8
# util
import imp, smtplib
from email.mime.text import MIMEText

def load_model_from_name(name):
	
	fp, pathname, description = imp.find_module(name)
	return imp.load_module('model5', fp, pathname, description)
	
def send_email(title, email_str):
	msg = MIMEText(email_str.encode('utf-8'), 'html', 'utf-8')
	msg['Subject'] = title.encode('utf-8')
	msg['From'] = 'tracholar_devtest@163.com'
	msg['To'] = '563876960@qq.com'

	s = smtplib.SMTP('smtp.163.com')
	pw = open('pw.pw','rb').read()
	s.login('tracholar_devtest@163.com',pw)
	s.sendmail(msg['From'], ['15155977600@139.com', '563876960@qq.com'], msg.as_string())
	s.quit()
def notify_me(msg):
	send_email(msg, msg)
	
if __name__ == '__main__':
	notify_me('test')