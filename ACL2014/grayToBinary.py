import sys,string

def grayToBinary(num):
	mask = num >> 1;
	while mask!=0:
		num = num ^ mask;
		mask = mask >> 1;
	return num;

num=grayToBinary(int(sys.argv[1],2))
print num
