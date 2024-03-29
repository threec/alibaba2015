# coding:utf-8
import csv

def GetDict(d, key):
	if key in d:
		return d[key]
	else:
		return 0

def CombineFeatureLabel(f_feature='feature.csv', f_label='label.csv', f_out='data.csv'):
	f1 = open(f_feature, 'rb')
	fr1 = csv.reader(f1, delimiter=',')

	f2 = open(f_label, 'rb')
	fr2 = csv.reader(f2, delimiter=',')

	f3 = open(f_out, 'wb')
	fw3 = csv.writer(f3, delimiter=',')

	user_item = dict()
	for row in fr2:
		key = '%s_%s' % (row[0],row[1])
		user_item[key] = row[2]
		
	header = fr1.next()
	header.append('buy')
	fw3.writerow(header)

	i = 0
	for row in fr1:
		key = '%s_%s' % (row[0],row[1])
		row.append( GetDict(user_item, key))
		fw3.writerow(row)
		i = i + 1
		if i%100000==0:
			print 'processed %d scores!' % i
			
	f1.close()
	f2.close()
	f3.close()
	
if __name__ == '__main__':
	CombineFeatureLabel('feature.merge.csv')