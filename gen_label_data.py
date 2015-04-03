# coding:utf-8
import csv

f = open('user_action_test.csv', 'rb')
fr = csv.reader(f, delimiter=',')

fd = open('label.csv', 'wb')
fw = csv.writer(fd, delimiter=',')

fr.next()
fw.writerow(['user_id', 'item_id', 'buy'])

user_item_buy = dict()

for row in fr:
	key = '%s_%s' % (row[0], row[1])
	
	
	if row[2] == '4':
		user_item_buy[key] = 1
	elif key not in user_item_buy:
		user_item_buy[key] = 0


		
for key, value in user_item_buy.items():
	uid, tid = key.split('_')
	data = [uid, tid, value]
		
	fw.writerow(data)
		

f.close()
fd.close()