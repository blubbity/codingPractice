#sorting robot shenanigans - Passes test case 2/2
# 24.01.22

def main():
	test_cases = int(input())
	for t in range(test_cases):
		num_cards = int(input())
		card_stack = []
		for n in range(num_cards):
			card_stack.append(input())
		cost = find_cost(card_stack)
		print("Case #{}: {}".format(t+1, cost))

def find_cost(card_list):
	cost = 0
	if len(card_list) > 1:
		for i in range(1, len(card_list)):
			if card_list[i-1] > card_list[i]:
				cost+=1
				card_list[i] = card_list[i-1]
	return cost

if __name__ == "__main__":
	main()