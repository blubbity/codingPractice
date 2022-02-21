#Passed test cases 2/2

LEFT = 0
RIGHT = 1

def main():
	test_cases = int(input())
	for test_case in range(1, test_cases+1):
		line = input()
		if line[0] == '1':
			n = int(line.split()[1])
			answer = find_nth(n)
		else:
			p = int(line.split()[1])
			q = int(line.split()[2])
			answer = find_position(p, q)
		print("Case #{}: {}".format(test_case, answer))


#---  Find nth ---#
def find_nth(n):
	directions = to_bin_path(n)
	p = 1
	q = 1
	for i in directions:
		p, q = branch(i, p, q)
	return "{} {}".format(p, q)

def to_bin_path(dec_num): #converts deciminal to binary, excluding most significant digit
# as 1 = 1, but 1 is the root of the tree so you don't choose a direction to get to 1
	digits = []
	while dec_num > 1:
		if dec_num % 2 == 0:
			digits = [0]+digits
		else:
			digits = [1]+digits
		dec_num = dec_num//2
	return digits

def branch(direction, p, q):
	if direction == LEFT:
		q = p+q
	elif direction == RIGHT:
		p = p+q
	return p, q


#--- Find Position ---#
def find_position(p, q):
	directions = get_directions(p, q)
	n = to_dec_position(directions)
	return n

def get_directions(p, q): #directions chosen in reverse order, i.e. if path is
#RIGHT, LEFT, RIGHT, LEFT, directions is [LEFT, RIGHT, LEFT, RIGHT]
	directions = []
	while p!=q:
		if p > q:
			directions.append(RIGHT)
			p = p-q
		else:
			directions.append(LEFT)
			q = q-p

	return directions

def to_dec_position(directions):
	binary = directions+[1] #is in reverse order
	total = 0
	for i in range(len(binary)):
		if binary[i] == 1:
			total += 2**i
	return total


if __name__ == '__main__':
	main()