# coding:utf-8

import csv, time,sys, util
import numpy as np



# 特征生成文件5

user_item_click_nobuy = dict()
user_item_star_nobuy = dict()
user_item_cart_nobuy = dict()
user_item_buy_again = dict()

user_item_click = set()
user_item_star = set()
user_item_cart = set()
user_item_buy = set()

user_item_last_click_time = dict()
user_item_last_star_time = dict()
user_item_last_cart_time = dict()
user_item_last_buy_time = dict()


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
def parse_time(t):
	return time.mktime(time.strptime(t,'%Y-%m-%d %H'))

def AddLastTime(time_dict, utid, t):
	if utid not in time_dict:
		time_dict[utid] = t
		return
	
	if DiffTime(time_dict[utid], t)<0:
		time_dict[utid] = t
		return
	
		
	
def JugeDoingNobuy(d,last_doing_set, last_doing_time, utid):
	if utid not in last_doing_set: # no doing
		d[utid] = 0
		return
	
	if utid not in user_item_buy: # not buy
		d[utid] = 1
		return
	
	
	do_t = last_doing_time[utid]
	buy_t = user_item_last_buy_time[utid]
	
	diff_time = DiffTime(do_t, buy_t)
	if diff_time > 0:
		d[utid] = 0 
		return
		
	d[utid] = 1
	# print utid
	
	
def GenFeature(finput='user_action_train.csv', foutput = 'feature.csv', lastday = '2014-12-18'):
	

	
	
	# 细化行为特征
	
	
	
	user_items = set()  # 其实是用户物品对
	item_cat = dict()

	with open(finput, 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		header = reader.next()
		print header
		
		i = 0
		for row in reader:
			uid = row[0]
			tid = row[1]
			cid = row[4]
			t = row[5]
			
			utid = '%s_%s' % (uid, tid)
			ucid = '%s_%s' % (uid, cid)
			
			user_items.add('%s_%s' % (uid,tid))
			item_cat[tid] = cid
			
			# diff_time = DiffTime('%s 00' % lastday, row[5]) + 24*24*3600
			
			
			
			
				
				
			if row[2] == '1': # click
				user_item_click.add(utid)
				AddLastTime(user_item_last_click_time, utid, t)
					
			if row[2] == '2': # star
				user_item_star.add(utid)
				AddLastTime(user_item_last_star_time, utid, t)
				
			if row[2] == '3': # add to car
				user_item_cart.add(utid)
				AddLastTime(user_item_last_cart_time, utid, t)
					
			if row[2] == '4':  # buy
				AddLastTime(user_item_last_buy_time, utid, t)
				
				
				if utid in user_item_buy:
					user_item_buy_again[utid] = 1
				else:
					user_item_buy.add(utid)
			
				
			i = i + 1
			if i%100000==0:
				print 'processed %d scores!' % i
	
	
			
	# user feature
	fd = open(foutput,'wb')
	fw = csv.writer(fd, delimiter=',')

	fw.writerow(['user_id', 'item_id',
		"user_item_click_nobuy",
		"user_item_star_nobuy",
		"user_item_cart_nobuy",
		"user_item_buy_again"
	])
	
	for key in user_items:
		uid, tid = key.split('_')
		cid = item_cat[tid]
		utid = '%s_%s' % (uid, tid)
		ucid = '%s_%s' % (uid, cid)
			
			
		JugeDoingNobuy(user_item_click_nobuy, user_item_click, user_item_last_click_time, utid)
		JugeDoingNobuy(user_item_star_nobuy, user_item_star, user_item_last_star_time, utid)
		JugeDoingNobuy(user_item_cart_nobuy, user_item_cart, user_item_last_cart_time, utid)
	
	
		data = [uid, tid,
			GetDict(user_item_click_nobuy, utid),
			GetDict(user_item_star_nobuy, utid),
			GetDict(user_item_cart_nobuy, utid),
			GetDict(user_item_buy_again, utid),
			]
		
		fw.writerow(data)
		
	fd.close()	


if __name__ == '__main__':
	fid = util.file_basename_id(__file__)
	if sys.argv[1]=='train':
		GenFeature('user_action_train.csv', 'feature%d.csv' % fid, lastday='2014-12-17')
	if sys.argv[1]=='submit':
		GenFeature('tianchi_mobile_recommend_train_user.csv', 'feature_total%d.csv' % fid, lastday='2014-12-18')