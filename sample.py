# coding:utf-8

import csv, sys

fname = sys.argv[1]
count = int(sys.argv[2])

fd = open('%s_sample.csv' % fname,'wb')
writer = csv.writer(fd, delimiter=',')
with open('%s.csv' % fname, 'rb') as f:
	reader = csv.reader(f, delimiter=',')
	i = 0
	for row in reader:
		writer.writerow(row)
		i = i+1
		if i==count:
			break
fd.close()