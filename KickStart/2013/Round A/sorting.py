#Passes test cases 2/2

def main():
	test_cases = int(input())
	for i in range(test_cases):
		n = int(input())
		books = input().split()
		worths = []
		for book in books:
			worth = int(book)
			worths.append(worth)
		ordered = order_shelf(worths)
		print("Case #{}: {}".format(i+1, ordered))

def order_shelf(worths):
	sorted_shelf = []
	a_worths = []
	b_worths = []
	for worth in worths:
		if worth%2 == 0:
			b_worths.append(worth)
		else:
			a_worths.append(worth)
	a_worths.sort()
	b_worths.sort(reverse=True)
	a_count = 0
	b_count = 0

	for i in range(len(worths)):
		worth = worths[i]
		if worth%2 == 0:
			sorted_shelf.append(b_worths[b_count])
			b_count += 1
		else:
			sorted_shelf.append(a_worths[a_count])
			a_count += 1

	bookshelf = ''
	for worth in sorted_shelf:
		bookshelf += ' '
		bookshelf += str(worth)

	return bookshelf

if __name__ == '__main__':
	main()