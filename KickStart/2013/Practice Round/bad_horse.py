#Passes test case 2/2

def main():
	test_cases = int(input(''))
	temp = []
	for i in range(test_cases):
		m = int(input(''))
		pairs = []
		for j in range(m):
			pair = input('').split()
			pairs.append(pair)
		is_possible = split_groups(pairs)
		temp.append(is_possible)
		#print("Case #{}: {}".format(i+1, is_possible))
	for i in range(test_cases):
		print("Case #{}: {}".format(i+1, temp[i]))

def split_groups(pairs):
	is_possible = True
	group1 = []
	group2 = []
	temp_pairs = pairs
	while len(temp_pairs) > 0:
		temp_pairs = []
		for pair in pairs:
			a = pair[0]
			b = pair[1]
			#If a is in a group check it doesn't also contain b. Then, if b
			#not already in there, add b to the other group
			if a in group1:
				if b in group1:
					is_possible = False
				if b not in group2:
					group2.append(b)
			elif a in group2:
				if b in group2:
					is_possible = False
				if b not in group1:
					group1.append(b)
			#If a isn't already in a group, check if b is in a group. If b is
			#in a group, add a to the other group.
			else:
				if b in group1:
					group2.append(a)
				elif b in group2:
					group1.append(a)
				#If neither a nor b are already in a group because groups are empty,
				#assign arbitrarily, else leave for later going through this loop again
				else:
					if len(group1)==0:
						group1.append(a)
						group2.append(b)
					else:
						temp_pairs.append(pair)
	if is_possible: 
		for pair in pairs:
			a = pair[0]
			b = pair[1]
			if a in group1 and b in group1:
				is_possible = False
				break
			elif a in group2 and b in group2:
				is_possible = False
				break

	if is_possible == True:
		answer = 'Yes'
	else:
		answer = 'No'
	return answer

if __name__ == '__main__':
	main()