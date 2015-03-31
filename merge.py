# coding:utf-8
# merge.py
# usage  python merge.py file1 file2
import csv, sys

if sys.argc!=4:
	print 'usage  python merge.py file1 file2 file3'
	
f1 = open(sys.argv[1], 'rb')
f2 = open(sys.argv[2], 'rb')
fr1 = csv.reader(f1, delimiter=',')
fr2 = csv.reader(f2, delimiter=',')

f = open(sys.argv[3], 'wb')
fw = csv.writer(f, delimiter=',')

