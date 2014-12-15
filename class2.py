#!/usr/bin/python
#Filename: class2.py
import string, pylab, cmd, datetime, math, os, sys, time, tkFileDialog, numpy
from string import *
from pylab import * 
from math import *

def Separator():		# 
	print "Create a file with the columns to plot\n"
	fileHandle = open( 'out.txt' , 'w')     
	filein = tkFileDialog.askopenfile(mode='r')
	print filein
	i=1
	while i < 14:
		line = filein.readline()
		i = i+1
	for line in filein.readlines():
               	if(line[0]=="#"):
                       	continue
        	year = int(line[0:4])
 		mont = int(line[5:7])
       		day  = int(line[8:10])
       		hour = int(line[11:13])
       		minu = int(line[14:16])
       		secs = float(line[17:23])
       		time = hour*3600+minu*60+secs
		n1 = line.find('|')
		n2 = line.find('|',n1+1)
		n3 = line.find('|',n2+1)
		n4 = line.find('|',n3+1)
		n5 = line.find('|',n4+1)
		n6 = line.find('|',n5+1)
		n7 = line.find('|',n6+1)
		n8 = line.find('|',n7+1)
		n9 = line.find('|',n8+1)
		m01 = line.find(',',n9+1)
		m02 = line.find(',',m01+1)
		n10 = line.find('|',m02+1)
		m11 = line.find(',',n10+1)
		m12 = line.find(',',m11+1)
		n11 = line.find('|',m12+1)
		m21 = line.find(',',n11+1)
		m22 = line.find(',',m21+1)
		n12 = line.find('|',m22+1)
		n13 = line.find('|',n12+1)
		m41 = line.find(',',n13+1)
		m42 = line.find(',',m41+1)
		m43 = line.find(',',m42+1)
		n14 = line.find('|',m43+1)
		m51 = line.find(',',n14+1)
		m52 = line.find(',',m51+1)
		m53 = line.find(',',m52+1)
		n15 = line.find('|',m53+1)
		m61 = line.find(',',n15+1)
		m62 = line.find(',',m61+1)
		m63 = line.find(',',m62+1)
		n16 = line.find('|',m63+1)
		m71 = line.find(',',n16+1)
		m72 = line.find(',',m71+1)
		m73 = line.find(',',m72+1)
		n17 = line.find('|',m73+1)
		m81 = line.find(',',n17+1)
		m82 = line.find(',',m81+1)
		m83 = line.find(',',m82+1)
		n18 = line.find('|',m83+1)
		m91 = line.find(',',n18+1)
		m92 = line.find(',',m91+1)
		m93 = line.find(',',m92+1)
		n19 = line.find('|',m93+1)
		mz1 = line.find(',',n19+1)
		mz2 = line.find(',',mz1+1)
		mz3 = line.find(',',mz2+1)
		n20 = line.find('|',mz3+1)
		ma1 = line.find(',',n20+1)
		ma2 = line.find(',',ma1+1)
		ma3 = line.find(',',ma2+1)
		n21 = line.find('|',ma3+1)
		mb1 = line.find(',',n21+1)
		mb2 = line.find(',',mb1+1)
		mb3 = line.find(',',mb2+1)
		n22 = line.find('|',mb3+1)
		mc1 = line.find(',',n22+1)
		mc2 = line.find(',',mc1+1)
		mc3 = line.find(',',mc2+1)
		n23 = line.find('|',mc3+1)
		md1 = line.find(',',n23+1)
		md2 = line.find(',',md1+1)
		md3 = line.find(',',md2+1)
		n24 = line.find('|',md3+1)
		me1 = line.find(',',n24+1)
		me2 = line.find(',',me1+1)
		me3 = line.find(',',me2+1)
		n25 = line.find('|',me3+1)
		mf1 = line.find(',',n25+1)
		mf2 = line.find(',',mf1+1)
		mf3 = line.find(',',mf2+1)
		n26 = line.find('|',mf3+1)
		mg1 = line.find(',',n26+1)
		mg2 = line.find(',',mg1+1)
		mg3 = line.find(',',mg2+1)
		n27 = line.find('|',mg3+1)
		mh1 = line.find(',',n27+1)
		mh2 = line.find(',',mh1+1)
		mh3 = line.find(',',mh2+1)
		n28 = line.find('|',mh3+1)
		mi1 = line.find(',',n28+1)
		mi2 = line.find(',',mi1+1)
		mi3 = line.find(',',mi2+1)
		n29 = line.find('|',mi3+1)
		mj1 = line.find(',',n29+1)
		mj2 = line.find(',',mj1+1)
		mj3 = line.find(',',mj2+1)
		n30 = line.find('|',mj3+1)
		mk1 = line.find(',',n30+1)
		mk2 = line.find(',',mk1+1)
		mk3 = line.find(',',mk2+1)
		n31 = line.find('|',mk3+1)
		ml1 = line.find(',',n31+1)
		ml2 = line.find(',',ml1+1)
		ml3 = line.find(',',ml2+1)
		n32 = line.find('|',ml3+1)
		mm1 = line.find(',',n32+1)
		mm2 = line.find(',',mm1+1)
		mm3 = line.find(',',mm2+1)
		n33 = line.find('|',mm3+1)
		mn1 = line.find(',',n33+1)
		mn2 = line.find(',',mn1+1)
		mn3 = line.find(',',mn2+1)
		n34 = line.find('|',mn3+1)
		mp1 = line.find(',',n34+1)
		mp2 = line.find(',',mp1+1)
		mp3 = line.find(',',mp2+1)
		n35 = line.find('|',mp3+1)
		mq1 = line.find(',',n35+1)
		mq2 = line.find(',',mq1+1)
		mq3 = line.find(',',mq2+1)
		n36 = line.find('|',mq3+1)
		mr1 = line.find(',',n36+1)
		mr2 = line.find(',',mr1+1)
		mr3 = line.find(',',mr2+1)
		n37 = line.find('|',mr3+1)
		n38 = line.find('|',n37+1)
		n39 = line.find('|',n38+1)
		n40 = line.find('|',n39+1)
		n41 = line.find('|',n40+1)
		n42 = line.find('|',n41+1)
		n43 = line.find('|',n42+1)
		tst = str(line[0:n1])
		azPos = str(line[n1+1:n2])
		elPos = str(line[n2+1:n3])
		azEnc0 = str(line[n3+1:n4])
		elEnc0 = str(line[n4+1:n5])
		disp0 = str(line[n5+1:n6])
		disp1 = str(line[n6+1:n7])
		disp2 = str(line[n7+1:n8])
		disp3 = str(line[n8+1:n9])
		xTilt0 = str(line[n9+1:m01])
		yTilt0 = str(line[m01+1:m02])
		temp0 = str(line[m02+1:n10])
		subRefAbsX = str(line[n37+1:n38])
		subRefAbsY = str(line[n38+1:n39])
		subRefAbsZ = str(line[n39+1:n40])
		subRefRotX = str(line[n40+1:n41])
		subRefRotY = str(line[n41+1:n42])
		print >> fileHandle,'%(TIMO)s %(AZP)s %(ELP)s %(AZE)s %(ELE)s %(Di0)s %(Di1)s %(Di2)s %(Di3)s %(XT0)s %(YT0)s %(TE0)s %(SRAx)s %(SRAy)s %(SRAz)s %(SRRx)s %(SRRy)s' % {'TIMO':time, 'AZP':azPos, 'ELP':elPos, 'AZE':azEnc0, 'ELE':elEnc0, 'Di0':disp0, 'Di1':disp1, 'Di2':disp2, 'Di3':disp3, 'XT0':xTilt0, 'YT0':yTilt0, 'TE0':temp0, 'SRAx':subRefAbsX, 'SRAy':subRefAbsY, 'SRAz':subRefAbsZ, 'SRRx':subRefRotX, 'SRRy':subRefRotY}
	fileHandle.close()
	filein.close()

def xtaz(Separator):
	print "Plot the XTilt0 as function of Azimuth data for given file\n"
	X=numpy.loadtxt('out.txt')
	azP = X[:,1]
       	xT0 = X[:,9]
       	title('"xTilt0 as function of Azimuth"', color = 'b')
       	pylab.ylabel('xTilt0(100*mV)')
       	plot(azP, xT0, 'r:s')
       	pylab.grid(True)
       	pylab.show()
	return

def disp0(Separator):
	print "Plot the disp0 as function of Azimuth data for given file\n"
	X=numpy.loadtxt('out.txt')
	azP=X[:,1]
	di0 = X[:,5]
       	title('"disp0 as function of Azimuth"', color = 'b')
       	pylab.ylabel('disp0(100*mV)')
       	plot(azP, di0, 'r:s')
       	pylab.grid(True)
       	pylab.show()
	return

def disp1(Separator):
	print "Plot the Linear Displacement 1 data as function of Az for given file\n"
	X=numpy.loadtxt('out.txt')
	azP=X[:,1]
	di1 = X[:,6]
        title('"LinSen1 as function of Azimuth"', color = 'b')
        pylab.xlabel('AZIMUTH(degrees)')
        pylab.ylabel('LinSen-1(100*mV)')
        plot(azP, di1, 'r:s')
        pylab.grid(True)
        pylab.show()
	return

def disp2(Separator):
	print "Plot the Linear Displacement 2 data as function of Az for given file\n"
	X=numpy.loadtxt('out.txt')
	azP=X[:,1]
	di2 = X[:,7]
        title('"LinSen2 as function of Azimuth"', color = 'b')
        pylab.xlabel('AZIMUTH(degrees)')
        pylab.ylabel('LinSen-2(100*mV)')
        plot(azP, di2, 'r:s')
        pylab.grid(True)
        pylab.show()
	return

def disp3(Separator):
	print "Plot the Linear Displacement 3 data as function of Az for given file\n"
	X=numpy.loadtxt('out.txt')
	azP=X[:,1]
	di3 = X[:,8]
        title('"LinSen3 as function of Azimuth"', color = 'b')
        pylab.xlabel('AZIMUTH(degrees)')
        pylab.ylabel('LinSen-3(100*mV)')
        plot(azP, di3, 'r:s')
        pylab.grid(True)
        pylab.show()
	return

def x0time(Separator):
	print "Plot the xTilt Meter 0 data as function of Time for given file\n"
	X=numpy.loadtxt('out.txt')
	time=X[:,0]
	xT0 = X[:,9]
        title('"Tilt Meter x0 as function of time in seconds"', color = 'b')
        pylab.xlabel('TIME(seconds)')
        pylab.ylabel('TiltMeter_x0(100*mV)')
        plot(time, xT0, 'r:s')
        pylab.grid(True)
        pylab.show()
	return

def d0time(Separator):
	print "Plot Linear Displacement 0 data as function of Time` for given file\n"
	X=numpy.loadtxt('out.txt')
	time=X[:,0]
	di0 = X[:,5]
        title('"Linear Displacement d0 as function of time"', color = 'b')
        pylab.xlabel('TIME(seconds)')
        pylab.ylabel('LinSen-0(100*mV)')
        plot(time, di0, 'r:s')
        pylab.grid(True)
        pylab.show()
	return
