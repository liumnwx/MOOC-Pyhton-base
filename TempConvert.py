tempstr = input()
if tempstr[0] in ['F']:
	c=(eval(tempstr[1:-1])-32)/1.8
	print("C{.2f}".format(c))
else tempstr[0] in ['C']
	f=1.8*eval(tempstr[1:-1])+32
	print("F{.2f}".format(f))