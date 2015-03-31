# coding:utf-8

import csv



# 用户总活跃度(所有行为次数之和)
# 最后一天活跃度(最后一天活跃次数)
# 用户转化率(购买次数/总行为次数)，
# 物品流行度(物品被行为的总和)
# 物品最后一天活跃度
# 物品转化率(被购买次数/总行为次数)
# 物品分类的流行度
# 物品分类的转化率
# 用户对该品牌的活跃度
# 用户对该品牌最后一天的活跃度
# 用户对该物品的活跃度
# 用户对该物品最后一天的活跃度

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

def GenFeature(finput='user_action_train.csv', foutput = 'feature.csv', lastday = '2014-12-18'):
	user_action_count = dict()
	user_lastday_count = dict()
	user_buy_count = dict()
	item_click_count = dict()
	item_lastday_count = dict()
	item_buy_count = dict()
	cat_click_count = dict()
	cat_buy_count = dict()
	user_cat_count = dict()
	user_cat_lastday_count = dict()
	user_item_count = dict()
	user_item_lastday_count = dict()

	user_items = set()
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
			
			user_items.add('%s_%s' % (uid,tid))
			item_cat[tid] = cid
			
			IncDict(user_action_count, uid)
			IncDict(item_click_count, tid)
			IncDict(cat_click_count, cid)
			IncDict(user_cat_count, '%s_%s' % (uid,cid))
			IncDict(user_item_count, '%s_%s' % (uid,tid))
			
			if row[5][:10]==lastday:  # lastday
				IncDict(user_lastday_count, uid)
				IncDict(item_lastday_count, tid)
				IncDict(user_cat_lastday_count, '%s_%s' % (uid,cid))
				IncDict(user_item_lastday_count, '%s_%s' % (uid,tid))
			if row[2] == '4':  # buy
				IncDict(user_buy_count, uid)
				IncDict(item_buy_count, tid)
				IncDict(cat_buy_count, cid)
				
			i = i + 1
			if i%100000==0:
				print 'processed %d scores!' % i
				
	# user feature
	fd = open(foutput,'wb')
	fw = csv.writer(fd, delimiter=',')

	fw.writerow(['user_id', 'item_id',"user_action_count", 
		"user_lastday_count", "user_buy_count", "item_click_count",
		"item_lastday_count", "item_buy_count", "cat_click_count", 
		"cat_buy_count", "user_cat_count", "user_cat_lastday_count", 
		"user_item_count", "user_item_lastday_count"])
	for key in user_items:
		uid, tid = key.split('_')
		cid = item_cat[tid]
		
		data = [uid, tid,
			GetDict(user_action_count, uid),
			GetDict(user_lastday_count, uid),
			GetDict(user_buy_count, uid),
			GetDict(item_click_count, tid),
			GetDict(item_lastday_count, tid),
			GetDict(item_buy_count, tid),
			GetDict(cat_click_count, cid),
			GetDict(cat_buy_count, cid),
			GetDict(user_cat_count, '%s_%s' % (uid, cid)),
			GetDict(user_cat_lastday_count, '%s_%s' % (uid, cid)),
			GetDict(user_item_count, '%s_%s' % (uid, tid)),
			GetDict(user_item_lastday_count, '%s_%s' % (uid, tid))]
		
		fw.writerow(data)
		
	fd.close()	


if __name__ == '__main__':
	GenFeature(lastday='2014-12-17')