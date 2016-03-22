# Examples for lists and loops lab

l0 = []
l1 = [1, "abc", 5.7, [1, 3, 5]]
l2 = [10, 11, 12, 13, 14, 15, 16]
l3 = [7, -5, 6, 27, -3, 0, 14]
M = 10
l4 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

all_pos = True #basics 1 
for x in l3:
	if x < 0:
		all_pos = False

pos_l3 = [] #loops and append 2 
for x in l3: 
	if x > 0:
		pos_l3.append(x)

n1 = [] #loops and append 3 
for x in l3:
	n1.append(x > 0)

n1 = [False] * len(l3) # 4
for i in range(len(n1)): 
	if l3[i] > 0:
		n1[i] = True
		
l5 = [0] * len(l4)
for i in range(len(l4)): 
	count = 0 
	for x in l4:
		if i == x: 
			count = count + 1 
	l5[i] = count
