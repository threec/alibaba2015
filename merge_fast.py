# coding:utf-8
import csv, sys, pandas
import numpy as np

if len(sys.argv)<4:
	print 'usage  python merge_fast.py f1 ... fn fo'
	
f = []
fr = []

fns = len(sys.argv)-2
for i in range(fns):
	fd = open(sys.argv[i],'rb')
	f.append(fd)
	reader = csv.reader(fd, delimiter=',')
	fr.append(reader)

fo = open(sys.argv[fns+1], 'wb')
fw = csv.writer(fo, delimiter=',')

header = fr[0].next()
for i in range(1,fns):
	header.append(fr[0].next()[2:])

fw.writerow(header)
nrows = 0
for row in fr[0]:
	for i in range(1,fns):
		row.append(fr[i].next()[2:])
	
	fw.writerow(row)
	nrows = nrows + 1
	if nrows%100000==0:
		print 'processed %d rows.' % nrows

for i in range(fns):
	f[i].close()
fo.close()

