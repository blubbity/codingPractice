#Passes test cases 2/2

tuples = {1:'',
		  2:'double ',
		  3:'triple ',
		  4:'quadruple ',
		  5:'quintuple ',
		  6:'sextuple ',
		  7:'septuple ',
		  8:'octuple ',
		  9:'nonuple ',
		  10:'decuple '
		 }
numbers = {'0':'zero ',
		   '1':'one ',
		   '2':'two ',
		   '3':'three ',
		   '4':'four ',
		   '5':'five ',
		   '6':'six ',
		   '7':'seven ',
		   '8':'eight ',
		   '9':'nine '
		 }

def main():
	test_cases = int(input())
	for i in range(test_cases):
		line = input().split()
		phone_number = line[0]
		dividing_format = line[1]
		number = split_number(phone_number, dividing_format)
		print("Case #{}: {}".format(i+1, number))

def split_number(number, format):
	format = format.split('-')
	phone_index = 0
	number_reading = ''
	for i in format:
		i = int(i)
		chunk = number[phone_index:phone_index+i]
		prev_digit = chunk[0]
		if i == 1:
			number_reading += numbers[prev_digit]
		else:
			counter = 1
			for j in range(1,i):
				current_digit = chunk[j]
				if current_digit == prev_digit:
					counter += 1
					if j == i-1:
						if counter < 11:
							number_reading += tuples[counter]
							number_reading += numbers[prev_digit]
						else:
							number_reading += counter*numbers[prev_digit]
						counter = 1
				else:
					if counter < 11:
						number_reading += tuples[counter]
						number_reading += numbers[prev_digit]
					else:
						number_reading += counter*numbers[prev_digit]
					if j == i-1:
						number_reading += numbers[chunk[j]]
					prev_digit = current_digit
					counter = 1
		phone_index = phone_index+i
	return number_reading.strip()

if __name__ == '__main__':
	main()