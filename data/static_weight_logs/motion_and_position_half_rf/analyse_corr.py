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


log_dir = "./"
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
	c = a[0:(1200000-offset)]-b[offset:1200000]
	means.append(numpy.mean(c))
	stds.append(numpy.std(c))
	
val, idx = min((val, idx) for (idx, val) in enumerate(stds))

offset = 10*idx
c = a[0:(1200000-offset)]-b[offset:1200000]
	
print len(c[20000:1100000-1:100])
plt.scatter(c[20000:1100000-1:100]-c[20000+1:1100000:100],a[20000:1100000-1:100]-a[20000+1:1100000:100],c=a[20000:1100000-1:100])
print numpy.corrcoef(c[20000:1100000-1]-c[20000+1:1100000],a[20000:1100000-1]-a[20000+1:1100000])
print numpy.corrcoef(c[20000:1100000-1]-c[20000+1:1100000],a[20000:1100000-1])
plt.show()

f = open("data.csv",'w') 

# write out
for i in xrange(len(c[20000:1100000-1:100])):
	n = 20000+i*100
	f.write("{0},{1},{2}\n".format(c[n]-c[n+1],a[n]-a[n+1],a[n]))
	
val, idx = min((val, idx) for (idx, val) in enumerate(stds))
print means[idx]
print val