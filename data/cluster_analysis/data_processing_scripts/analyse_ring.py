#!/usr/bin/python
# Analyses weight data from model and generates preferred RF directions
# Must be placed in the same directory as the log data

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

print 'geting ring weight data'


ts = []
log_dir = "./"
log = sml_log_parser.sml_log(log_dir, 'landmark_l_to_CBL_Synapse_0_weight_update_w_logrep.xml')
for j in xrange(0,8):
	for i in xrange(0,16):
		data = log.getdataforindex(i+j*16)
		if i == 0:
			s = (numpy.array(data)*numpy.sin(0))[0:-1:10]
			c = (numpy.array(data)*numpy.cos(0))[0:-1:10]
		else:
			s = s + (numpy.array(data)*numpy.sin(20*i/180.0*math.pi))[0:-1:10]
			c = c + (numpy.array(data)*numpy.cos(20*i/180.0*math.pi))[0:-1:10]
	t = numpy.arctan2(s,c)
	ts.append(t)
filename = "./datal"
f = open(filename, "w")
for x in xrange(len(ts[0])):
	for y in xrange(len(ts)):
		f.write("{0},".format(ts[y][x]*180.0/math.pi))
	f.write("\n")

ts = []
log = sml_log_parser.sml_log(log_dir, 'landmark_r_to_CBL_Synapse_0_weight_update_w_logrep.xml')
for j in xrange(0,8):
	for i in xrange(0,16):
		data = log.getdataforindex(i+j*16)
		if i == 0:
			s = (numpy.array(data)*numpy.sin(0))[0:-1:10]
			c = (numpy.array(data)*numpy.cos(0))[0:-1:10]
		else:
			s = s + (numpy.array(data)*numpy.sin(20*i/180.0*math.pi))[0:-1:10]
			c = c + (numpy.array(data)*numpy.cos(20*i/180.0*math.pi))[0:-1:10]
	t = numpy.arctan2(s,c)
	ts.append(t)
filename = "./datar"
f = open(filename, "w")
for x in xrange(len(ts[0])):
	for y in xrange(len(ts)):
		f.write("{0},".format(ts[y][x]*180.0/math.pi))
	f.write("\n")
	
