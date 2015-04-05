# coding:utf-8
# util
import imp, smtplib, os, re, time, pickle
from email.mime.text import MIMEText

def file_basename(fn):
	fname = os.path.basename(fn)
	fname = fname[:fname.rindex('.')]
	return fname
def file_basename_id(fn):
	fname = file_basename(fn)
	fid = re.search('\d+', fname)
	if fid is None:
		return 1

	return int(fid.group())
	
	
def IncDict(d, key):
	if key in d:
		d[key] = d[key] + 1
	else:
		d[key] = 1

def GetDict(d, key):
	if key in d:
		return d[key]
	else:
		return 0
def DiffTime(t1, t2):
	t1 = time.mktime(time.strptime(t1,'%Y-%m-%d %H'))
	t2 = time.mktime(time.strptime(t2,'%Y-%m-%d %H'))
	return t1 - t2


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
def save_obj(obj, fn):
	f = open(fn, 'wb')
	pickle.dump(obj, f)
	f.close()
def load_obj(fn):
	f = open(fn, 'rb')
	obj = pickle.load(f)
	f.close()
	return obj
	
if __name__ == '__main__':
	notify_me('test')