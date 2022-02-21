"""Given a 4X4 grid of letters and a dictionary of words at least 3 letters
long, find the longest word from the dictionary that can be formed in the
grid. You can start at any position on the board, and move in any of the
up to 8 direcetions to choose another letter (cannot return to same grid
position to reuse a letter in the same word).

You are given a dictionary, with two helper functions:
    isWord() to check if a word is valid and
    isPrefix() to check if a string is a prefix of some valid word.""" 


# Main function to find longest word in dictionary
def find_longest(grid, dictionary):
	starts = [[0, 0], [0, 1], [0, 2], [0, 3]
			  [1, 0], [1, 1], [1, 2], [1, 3]
			  [2, 0], [2, 1], [2, 2], [2, 3]
			  [3, 0], [3, 1], [3, 2], [3, 3]
			 ]
	for row in range(4):
		for col in range(4):
			start = grid[row][col]
			words = traverse(grid, dictionary, starts, [])
			longest = longest_word(words)
	return longest


# Traverse through the grid, and collect valid words in a list
def traverse(grid, dictionary, words_coordinates, words):
	for word_coordinates in words_coordinates:
		word = coordinates_to_words(grid, word_coordinates)
		if isWord(word, dictionary):
			words.append(word) #add valid word to list of words
		if isPrefix(word, dictionary): #could become valid word, so go down branches
			branches = flood_branches(word_coordinates)
			if branches:
				traverse(grid, dictionary, branches, words)
		#else, no potential to become a valid word
		return words


# Return a list of up to 8 branches word can branch to
def flood_branches(word_coordinates):
	branches = []
	current_tile = word_coordinates[-1]
	x = current_tile[0]
	y = current_tile[1]
	# Generates coordinates for tile + 8 surrounding tiles
	for i in range(-1, 2):
		new_x = x+i
		if new_x >= 0 and new_x <= 4: # If tile still in grid
			for j in range(-1, 2):
				new_y = y+j
				if new_y >= 0 and new_y <= 4:
					# If letter tile hasn't already been used, create a branch with it
					if [new_x, new_y] not in word_coordinates:
						coordinates = []
						for coordinate in word_coordinates:
							coordinates.append(coordinate)
						coordinates.append([new_x, new_y])
						branches.append(coordinates)
	return branches


# Converts list of tile coordinates into string
def coordinates_to_words(grid, coordinates):
	word = ''
	for coordinate in coordinates:
		char = grid[coordinate[0], coordinate[1]]
		word += char
	return word


# Returns the longest word from a list of words. If multiple longest words,
# return first alphabetically.
def longest_word(words):
	longest_word = ''
	for word in words:
		if len(word) > len(longest_word):
			longest_word = word
		elif len(word) == len(longest_word):
			if word < longest_word:
				longest_word = word
	return longest_word