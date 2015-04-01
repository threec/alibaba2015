# coding:utf-8
import csv
from random import random, seed

def DataSplit(fin = 'data.csv', ftrain = 'data_train.csv', ftest='data_test.csv', train_rate=0.75):
	f = open(fin, 'rb')
	fr = csv.reader(f, delimiter=',')

	fo1 = open(ftrain, 'wb')
	fw1 = csv.writer(fo1, delimiter=',')
	fo2 = open(ftest, 'wb')
	fw2 = csv.writer(fo2, delimiter=',')

	seed(44)

	header = fr.next()
	fw1.writerow(header)
	fw2.writerow(header)

	i = 0
	for row in fr:
		if random()>train_rate:
			fw2.writerow(row)
		else:
			fw1.writerow(row)
		i = i + 1
		if i%100000==0:
			print 'processed %d row!' % i
			
	f.close()
	fo1.close()
	fo2.close()

if __name__ == '__main__':
	DataSplit()