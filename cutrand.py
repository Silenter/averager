#!/usr/bin/env python

import wave
import random
import sys

try:
  filename = sys.argv[1] 
except IndexError:
  filename = './test.wav'
fp = wave.open(filename)
wavelength = fp.getnframes()
left = wavelength - fp.tell()
box = []
while left > 0:
	cliplength = min(random.randint(1,1000000), left)
	sample = fp.readframes(cliplength)
	cutpoint = len(sample)/2
	cutpoint = cutpoint + cutpoint % 2
	print "cliplength: " + str(cliplength)
	print "sample length: " + str(len(sample))
	print "cutpoint = " + str(cutpoint)
        box.append(sample[cutpoint:]) 
        box.append(sample[:cutpoint])
	left = wavelength - fp.tell()

fp2 = wave.open('./'+filename+'.cutup.wav', 'w')
fp2.setparams(fp.getparams())
fp.close()

random.shuffle(box)
for sample in box:
  fp2.writeframesraw(sample)
fp2.close()
