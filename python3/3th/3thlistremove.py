def outputlist(ls):
	for l in ls:
		print(l)
	print()


ll = [11, 22, 'cc', [11, 22, 33, 44], [22, 11, 33, 44]]

outputlist(ll)
ll.remove(22)
outputlist(ll)

ll.remove(11)
outputlist(ll)

ll.remove(33)
outputlist(ll)
