#Passes test case 1/1

import math

def main():
	test_cases = int(input())
	for i in range(test_cases):
		vals = input().split()
		v = int(vals[0])
		d = int(vals[1])
		o = get_angle(v, d)
		print("Case #{}: {}".format(i+1, o))

#s=ut+0.5at^2
#o=0.5(sin^-1(9.8d/v^2))
def get_angle(velocity, distance):
	thing = 9.8*distance/(velocity*velocity)
	if thing>1:
		thing = 1
	elif thing<-1:
		thing = -1
	angle = 0.5*(math.asin(thing))
	return math.degrees(angle)

if __name__ == '__main__':
	main()