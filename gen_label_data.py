# coding:utf-8
import csv

f = open('user_action_test.csv', 'rb')
fr = csv.reader(f, delimiter=',')

fd = open('label.csv', 'wb')
fw = csv.writer(fd, delimiter=',')

fr.next()
fw.writerow(['user_id', 'item_id', 'buy'])
for row in fr:
	data = [row[0], row[1], 0]
	if row[2] == '4':
		data[2] = 1
	fw.writerow(data)
		

f.close()
fd.close()