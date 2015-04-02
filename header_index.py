# coding:utf-8
import csv,sys,os
if len(sys.argv)<2:
	fn = 'data.csv'
else:
	fn = sys.argv[1]
f = open(fn,'rb')
fr = csv.reader(f, delimiter=',')

header = fr.next()
f.close()

print 'File: %s\n' % fn
for i in range(len(header)):
	print i, header[i]
	
