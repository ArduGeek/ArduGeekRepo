import wave, struct, math, random, numpy
sampleRate = 44100.0
duration = 100.0
frequency = 440.0
obj = wave.open('sound.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
audio = []
math_sine = []
values = numpy.arange(0, 6.28, 0.1)
for d in values:
	var1 = int(10000*numpy.sin(d))
	print(var1)
	math_sine.append(var1)
for a in range(10000):
	for b in math_sine:	
		audio.append(b)
for c in audio:
	data = struct.pack('<h', c)
	obj.writeframesraw( data )
obj.close()

