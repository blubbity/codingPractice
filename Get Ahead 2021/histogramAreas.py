"""Given an array of non-negative integers that represent the bars
(y value) in a histogram (with the array index being the x value),
find the rectangle with the largest area under the curve and above the
x-axis (i.e. the largest rectangle that fits inside the histogram).
Return the pair of array indices that represent the rectangle."""


def maximum_rectangle(bars):
	max_area = 0
	indice_pair = []
	# Dictionary of {height : [indices of bars at that height]}
	values = {}
	# Load values into dictionary
	for i in range(len(bars)):
		height = bars[i]
		if height in values:
			values[height].append(i)
		else:
			values[height] = [i]

	# Check rectangles by ascending height
	shorter = [0]*(len(bars)+1)#Turn to 1 if bar at index is shorter than height
	shorter[-1] = 1 #Set a 'shorter' boundary at the end, so we keep rectangle
				    #within the histogram
	heights = list(values.keys())
	heights.sort()
	for height in heights:
		width_start = 0 #Keep track of index at start of width
		width = 0
		for i in range(len(shorter)):
			if shorter[i] == 0:
				width += 1
			else: #bar is shorter, cutting off the rectangle horizontally
				area = width*height
				if area > max_area:
					max_area = area
					indice_pair = [width_start, i-1]
				width = 0
				width_start = i+1 #Start of rectangle is at least the next index
		# Update indices shorter than the next height
		for index in values[height]:
			shorter[index] = 1
	return indice_pair


def test():
	assert maximum_rectangle([6, 2, 5, 4, 5, 1, 6]) == [2, 4]
	assert maximum_rectangle([2, 4, 2, 1]) == [0, 2]
	assert maximum_rectangle([2, 4, 2, 1, 10, 6, 10]) == [4, 6]


if __name__ == '__main__':
	test()