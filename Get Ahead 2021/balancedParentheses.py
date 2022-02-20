""" Given a string of parentheses, find the size of the longest
contiguous substring of balanced parentheses. Parentheses are
considered balanced when there is a valid closing parenthesis for an
opening one. """
# Note: considered (())() to be 6 continuous parenthesis, not 4 and 2

def test():
	assert find_max_len("()") == 2
	assert find_max_len("())(())") == 4
	assert find_max_len(")(()))))((((()") == 4
	assert find_max_len("(((())))") == 8
	assert find_max_len(")(((((((") == 0
	assert find_max_len("()(") == 2
	assert find_max_len("())") == 2
	assert find_max_len("(()())") == 6
	assert find_max_len("())(())") == 4
	assert find_max_len(")(()))))(((()") == 4
	assert find_max_len("(())((((()((()") == 4
	assert find_max_len("((()()()())(()()())(()())(()))") == 30


def find_max_len(string):
	unpaired_open_brackets = []
	unpaired_close_brackets = []
	max_length = 0

	# Pair off brackets
	for i in range(1, len(string)+1): #Offset by 1 to later measure gap
	#between indices
		if string[i-1] == '(':
			unpaired_open_brackets.append(i)
		else:
			if len(unpaired_open_brackets) > 0:
				unpaired_open_brackets.pop()
			else:
				unpaired_close_brackets.append(i)
	unpaired_brackets = unpaired_open_brackets+unpaired_close_brackets
	unpaired_brackets.sort()

	# Measure gap between unpaired brackets
	if len(unpaired_brackets) == 0: #All brackets pair
		max_length = len(string)
	else:
		#Set boundaries at start and end of string
		if unpaired_brackets[0] != 1:
			unpaired_brackets = [0] + unpaired_brackets
		if unpaired_brackets[-1] != len(string):
			unpaired_brackets += [len(string)+1]
		#Measure gap between boundaries
		for i in range(1, len(unpaired_brackets)):
			unpaired = unpaired_brackets[i]
			prev_unpaired = unpaired_brackets[i-1]
			gap = unpaired - prev_unpaired - 1 #because gap is exclusive
			if gap > max_length:
				max_length = gap

	return max_length



if __name__ == "__main__":
	test()