filename='micsweep46s'

import csv
from scipy.fftpack import rfft, rfftfreq
from scipy.io import wavfile
from matplotlib import pyplot as plt
from scipy.signal import savgol_filter,find_peaks
import numpy as np

def normalize(arr):
	mx=max(arr)
	for i in range(0,len(arr)):
		arr[i]/=mx
	return arr

def rmdup(a,b):
	freqs=[]
	amp=[]
	for i in range(0,len(a)):
		if(a[i] in freqs):
			continue
		freqs.append(a[i])
		amp.append(b[i])
	return [freqs,amp]

def f(a,b,freqarr):
	freqs=[]
	amp=[]
	idx=0
	pad=1
	i=0
	while(pad<=22000):
		while(i<len(freqarr) and freqarr[i]<pad):
			while(a[idx]<freqarr[i]):
				idx+=1
			freqs.append(freqarr[i])
			amp.append(b[idx])
			i+=1
		while(a[idx]<pad):
			idx+=1
		freqs.append(pad)
		amp.append(b[idx])
		pad+=1
	return [freqs,amp]

def todb(a):
	for i in range(0,len(a)):
		a[i]=20*np.log10(np.abs(a[i]))
		a[i]=a[i]*-1
	return a

def findpeak(a,b):
	freqs=[]
	amps=[]
	idx=find_peaks(b)[0]
	for i in idx:
		freqs.append(a[i])
		amps.append(b[i])
	return [freqs,amps]

def forsweep(a):
	i=0
	num=1073
	arr=[]
	for i in a:
		arr.append(i/num)
	return arr


SAMPLE_RATE,normalized_tone=wavfile.read(filename+'.wav')

N = len(normalized_tone)
yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)
yf=forsweep(yf)
yf=np.abs(yf)
xf,yf=findpeak(xf,yf)

#xf,yf=findpeak(xf,yf)
#plt.plot(xf,yf)
#plt.show()

freqarr=[]
with open('zero.csv', mode='r') as input:
	reader=csv.reader(input, delimiter=',')
	for row in reader:
		freqarr.append(float(row[0]))

yf=normalize(yf)
xf,yf=f(xf,yf,freqarr)
xf,yf=rmdup(xf,yf)
plt.plot(xf,yf)


yf=savgol_filter(yf,101,2)
yf=normalize(yf)

plt.plot(xf,yf)

plt.show()
yf=todb(yf)

with open(filename+'.csv', mode='w', newline='') as output:
	writer=csv.writer(output,delimiter=',')
	writer.writerow(['frequency','raw'])
	for i in range(0,len(xf)):
		writer.writerow([xf[i],yf[i]])