#!/usr/bin/python

import xml.etree.ElementTree as ET
import sml_log_parser
from subprocess import call, Popen
import os.path
import os
import time, stat, random, math
import ctypes
import struct
import csv
import numpy
from os import listdir
import matplotlib.pyplot as plt

print 'Analyse the correlation between the ring and world position'

log_dirs=["runA","runB","runC","runD","runE", \
					"runF","runG","runH","runI","runJ"]

corr_EvC = []
corr_EvA = []

for log_dir in log_dirs:
	log = sml_log_parser.sml_log(log_dir, 'changes_for_batch_a_logrep.xml')
	data = log.getdataforindex(0)
	#print len(data)
	a = numpy.array(data)

	log = sml_log_parser.sml_log(log_dir, 'ring_direction_av_logrep.xml')
	data = log.getdataforindex(0)
	#print len(data)
	b = numpy.array(data)
				
	#test offsets to find min
	means = []
	stds = []
	for offset in xrange(0,600,10): 				
		c = a[0:(598000-offset)]-b[offset:598000]
		means.append(numpy.mean(c))
		stds.append(numpy.std(c))
	
	val, idx = min((val, idx) for (idx, val) in enumerate(stds))

	offset = 10*idx
	c = a[0:(598000-offset)]-b[offset:598000]
	
	print len(c[20000:580000-1:100])
	plot = plt.figure()
	plt.scatter(c[20000:580000-1:100]-c[20000+1:580000:100],a[20000:580000-1:100]-a[20000+1:580000:100],c=a[20000:580000-1:100])
	print numpy.corrcoef(c[20000:580000-1]-c[20000+1:580000],a[20000:580000-1]-a[20000+1:580000])[0,1]
	print numpy.corrcoef(c[20000:580000-1]-c[20000+1:580000],a[20000:580000-1])[0,1]
	
	corr_EvC.append(numpy.corrcoef(c[20000:580000-1]-c[20000+1:580000],a[20000:580000-1]-a[20000+1:580000])[0,1])
	corr_EvA.append(numpy.corrcoef(c[20000:580000-1]-c[20000+1:580000],a[20000:580000-1])[0,1])

plt.show()

f = open("corr_mean_sd.csv",'w') 

print numpy.mean(corr_EvC)
print numpy.std(corr_EvC)

# write out
for i in xrange(len(corr_EvC)):
	f.write("{0},{1}\n".format(corr_EvC[i], corr_EvA[i]))

f2 = open("corr_all.csv",'w')

for i in xrange(len(c[20000:1100000-1:100])):
	n = 20000+i*100
	f2.write("{0},{1},{2}\n".format(c[n]-c[n+1],a[n]-a[n+1],a[n]))