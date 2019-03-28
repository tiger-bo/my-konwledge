#！/usr/bin/python3

stus = {"001":{"name": 'zzy',"shuxue":88,"yuwen":77,"yingyu":66},\
"002":{"name": 'zzx',"shuxue":55,"yuwen":66,"yingyu":77},\
"003":{"name": 'zzx',"shuxue":55,"yuwen":66,"yingyu":77}}

for s, i in stus.items():
	print("stunum: " + s)
	for k , info in i.items():
		print(k, ":", info)
	print("==========")


ll = ['aa', 'bb', 'cc']

def outputlist(ls):
	for l in ls:
		print(l)
	print()


def inputlist(ls,v):
	ls.append(v)

outputlist(ll)

inputlist(ll,'qq')
inputlist(ll,{"name":"aa","shuxue":6})
outputlist(ll)

ll.extend(ll)
outputlist(ll)

ll.pop()
outputlist(ll)

ll.pop(0)
outputlist(ll)


print("bb count:", ll.count("bb"))

print(ll.index("cc"))

del ll[0]
outputlist(ll)
print()

yy = ('11','22', 33)

outputlist(yy)
