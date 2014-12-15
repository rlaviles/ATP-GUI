#!/usr/bin/python
# Filename: class3.py
import string, pylab, cmd, datetime, math, os, sys, time, tkFileDialog, tkMessageBox, numpy
from string import *
from pylab import * 
from math import *

def Creator():
   print "Create an output file with the columns to plot\n"
   fileHandle=open( 'pscout.txt' , 'w')
   filein = tkFileDialog.askopenfile(mode='r')
   print filein
   i=1
   while i < 14:
    line = filein.readline()
    i = i+1
   for line in filein.readlines():
    if(line[0]=="#"):
     continue
    try:
     utc = line[0:11]
     ho = int(line[0:2])
     mi = int(line[3:5])
     se = float(line[6:11])
     ti = ho*3600+mi*60+se
     az_c= float(line[13:23])
     el_c= float(line[25:33])
     az_m= float(line[35:45])
     el_m= float(line[47:55])
     az_o= float(line[57:67])
     el_o= float(line[69:77])
     az_e= float(line[79:89])
     el_e= float(line[91:99])
    except ValueError:
     if("ValueError: need more than 1 value to unpack"):
      print('You had chosen a wrong kind of file: pick an acuReport file!!\n')
      tkMessageBox.showwarning(
            "Open an acuReport file",
            "You had chosen a wrong file. Please pick an acuReport file!\n")
      break
     elif("ValueError: invalid literal for float(): invali"):
      continue
    print >> fileHandle,'%(TI)5.5f %(AZc)4.6f %(ELc)4.6f %(AZo)4.6f %(ELo)4.6f ' % {'TI':ti,'AZc':az_c,'ELc':el_c,'AZo':az_o,'ELo':el_o}
   fileHandle.close()
   filein.close()

# End of Creator function

def az_onvsco(Creator):
	X=numpy.loadtxt('pscout.txt')
	ti = X[:,0]
	azc= X[:,1]
	az = X[:,3]
	elc= X[:,2]
	el = X[:,4]
	title('"On TE AZ .vs. Commanded AZ as function of time (s)"', color = 'b')
	pylab.xlabel('time (s)')
	pylab.ylabel('AZ(degrees)')
	plot(ti, az, 'r:s',ti,azc,'g:o')
	pylab.grid(True)
	pylab.show()
	return

def el_onvsco(Creator):	
	X=numpy.loadtxt('pscout.txt')
	ti = X[:,0]
	azc= X[:,1]
	az = X[:,3]
	elc= X[:,2]
	el = X[:,4]
	title('"On TE EL .vs. Commanded EL as function of time (s)"', color = 'b')
	pylab.xlabel('time (s)')
	pylab.ylabel('EL(degrees)')
	plot(ti, el, 'r:s',ti,elc,'g:o')
	pylab.grid(True)
	pylab.show()
	return

def azel_onvsco(Creator):
	X=numpy.loadtxt('pscout.txt')
	ti = X[:,0]
	azc= X[:,1]
	az = X[:,3]
	elc= X[:,2]
	el = X[:,4]
	subplot(211)
	title('"On TE AZ .vs. Commanded AZ as function of time (s)"', color = 'b')
	pylab.xlabel('time (s)')
	pylab.ylabel('AZ(degrees)')
	plot(ti, az, 'r:s',ti,azc,'g:o')
	pylab.grid(True)
	subplot(212)
	title('"On TE EL .vs. Commanded EL as function of time (s)"', color = 'b')
	pylab.xlabel('time (s)')
	pylab.ylabel('EL(degrees)')
	plot(ti, el, 'r:s',ti,elc,'g:o')
	pylab.grid(True)
	pylab.show()
	return

def az_diff_onvsco(Creator):
	X=numpy.loadtxt('pscout.txt')
	ti = X[:,0]
	azc= X[:,1]
	az = X[:,3]
	elc= X[:,2]
	el = X[:,4]
	title("Difference AZcommanded - AZonTE versus time", color ='b')
	pylab.xlabel('time (s)')
	pylab.ylabel('difference(degrees)')
	plot(ti, (azc-az), 'r:s')
	pylab.grid(True)
	pylab.show()
	return

def el_diff_onvsco(Creator):
	X=numpy.loadtxt('pscout.txt')
	ti = X[:,0]
	azc= X[:,1]
	az = X[:,3]
	elc= X[:,2]
	el = X[:,4]
	title("Difference ELcommanded - ELonTE versus time", color ='b')
	pylab.xlabel('time (s)')
	pylab.ylabel('difference(degrees)')
	plot(ti, (elc-el), 'r:s')
	pylab.grid(True)
	pylab.show()
	return
