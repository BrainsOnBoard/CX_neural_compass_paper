#!/usr/bin/python
# Analyses weight data from model after analyse_ring.py and clusters RF preferred directions
# Must be placed in the same directory as the log data
# analyse_ring.py must be run first

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


from numpy import genfromtxt

from sklearn.cluster import DBSCAN
from sklearn import metrics

print 'getting clustering'

# where we'd expect the RFs to lie in a retinatopic mapping
offsets = [168.75,146.25,123.75,101.25,78.75,56.25,33.75,11.25,-11.25,-33.75,-56.25,-78.75,-101.25,-123.75,-146.25,-168.75]

datar = genfromtxt('./datar', delimiter=',')
datal = genfromtxt('./datal', delimiter=',')

datar = datar[::10,0:8]
datal = datal[::10,0:8]

print datar.shape

# concat
data = numpy.hstack((datal,numpy.fliplr(datar)))

clusters = []
unclustered = []
cluster_locs = []
cluster_sizes = []

for row in data:
	curr_line = row-offsets


	#print curr_line

	# convert to x,y
	c_line = numpy.transpose(numpy.cos(numpy.deg2rad(curr_line)))
	s_line = numpy.transpose(numpy.sin(numpy.deg2rad(curr_line)))


	xy_line = numpy.vstack((c_line,s_line))

	xy_line = numpy.transpose(xy_line)



	# cluster
	db = DBSCAN(eps=0.25, min_samples=2).fit(xy_line)

	core_samples_mask = numpy.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_
	

	# Number of clusters in labels, ignoring noise if present.
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	
	n_unclustered = numpy.sum(labels<0)
	#print('Estimated number of clusters: %d' % n_clusters_)
	
	cluster_locs_temp = []
	cluster_sizes_temp = []
	
	# locate the clusters
	for i in xrange(n_clusters_):
		# sum all indices for that cluster
		vals = xy_line[labels==i,:]
		num = numpy.sum(labels==i)
		c_s = numpy.sum(vals[:,0])
		s_s = numpy.sum(vals[:,1])
		
		cluster_locs_temp.append(numpy.rad2deg(numpy.arctan2(c_s, s_s)))
		cluster_sizes_temp.append(num)
	
	cluster_sizes.append(cluster_sizes_temp)
	cluster_locs.append(cluster_locs_temp)
	clusters = numpy.append(clusters, n_clusters_)
	unclustered = numpy.append(unclustered, n_unclustered)
	
print data[-1,:]-offsets
	

plt.plot(clusters,'r')
plt.plot(unclustered,'b')
plt.title("Cluster numbers over time", fontsize=20)
plt.xlabel('time')
plt.ylabel('n clusters')

fig2 = plt.figure()	

cluster_locs_big = []
cluster_num_big = []
print len(cluster_locs)

for i in xrange(len(cluster_locs)):
	for j in xrange(len(cluster_locs[i])):
		cluster_locs_big.append([i,cluster_locs[i][j]])
		cluster_num_big.append(cluster_sizes[i][j]*4)
		
d = numpy.asarray(cluster_locs_big)

plt.scatter(d[:,0],d[:,1],s=cluster_num_big)

plt.show()