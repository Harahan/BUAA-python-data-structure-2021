import random


def test(x, y, z):
	inf = 2147483647
	
	q, arr, buf = [x, y, z], [], []
	
	data = open("data.txt", "w")
	data1 = open("data1.txt", "w")
	data2 = open("data2.txt", "w")
	data3 = open("data3.txt", "w")
	data.write(str(x + y + z) + "\n")
	o = 0
	temp = [str(o), str(q[o])]
	while o <= 2:
		data.write(temp[1] + "\n" + temp[0] + "\n")
		
		if int(temp[0]) == 0:
			buf = random.sample(range(-inf, inf), int(temp[1]))
			arr.extend(buf)
			j = 0
			while j < int(temp[1]):
				data1.write(str(buf[j]) + "\n")
				data2.write(str(buf[j]) + "\n")
				data3.write(str(buf[j]) + "\n")
				j += 1
		
		elif int(temp[0]) == 2:
			buf = random.sample(arr, int(temp[1]))
			j = 0
			while j < int(temp[1]):
				data1.write(str(buf[j]) + "\n")
				data2.write(str(buf[j]) + "\n")
				data3.write(str(buf[j]) + "\n")
				j += 1
		
		else:
			buf = random.sample(arr, int(temp[1]))
			j = 0
			while j < int(temp[1]):
				data1.write(str(buf[j]) + "\n")
				data2.write(str(buf[j]) + "\n")
				data3.write(str(buf[j]) + "\n")
				j += 1
		o += 1
		if o < len(q):
			temp = [str(o), str(q[o])]
	
	for i in arr:
		data1.write(str(i) + "\n")
		data2.write(str(i) + "\n")
		data3.write(str(i) + "\n")
	
	data.close()
	data1.close()
	data2.close()
	data3.close()
