#!/usr/bin/env python

import wave
import random
import sys

try:
  filename = sys.argv[1] 
except IndexError:
  filename = './test.wav'
fp = wave.open(filename)
fp2 = wave.open('./'+filename+'-cutup.wav', 'w')
fp2.setparams(fp.getparams())
wavelength = fp.getnframes()
left = wavelength - fp.tell()
while left > 0:
	cliplength = min(random.randint(1,100000), left)
	sample = fp.readframes(cliplength)
	cutpoint = len(sample)/2
	cutpoint = cutpoint + cutpoint % 2
	print "cliplength: " + str(cliplength)
	print "sample length: " + str(len(sample))
	print "cutpoint = " + str(cutpoint)
	sample = sample[cutpoint:] + sample[:cutpoint]
	fp2.writeframesraw(sample)
	left = wavelength - fp.tell()
fp.close()
fp2.close()
