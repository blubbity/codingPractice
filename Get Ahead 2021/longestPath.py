"""Write a function that computes the length of the longest path of
consecutive integers in a tree. Integers are all positive and appear
only once in the tree.
 
A node in the tree has a value and a set of children nodes. A tree has
no cycles and each node has exactly one parent."""

class Tree:
	def __init__(self, value, children = []): #children is a list of child nodes
		self.value = value
		self.children = children


def longest_path(tree):
	if tree == None: #Base case, no tree given
		return 0
	else:
		longest_length = max(traverse(tree, tree.value-1, 0, []))
		#parent_value given as tree.value-1, because we are giving the recursive
		#function the head of the tree, which doesn't have a parent, so we're
		#fabricating that so it's considered consecutive
		return longest_length


def traverse(tree, parent_value, parent_path_length, ls_lens):
	if tree.value == parent_value+1 or tree.value == parent_value-1:
		path_length = parent_path_length + 1
	else:
		path_length = 1
	ls_lens.append(path_length)
	for child in tree.children:
		traverse(child, tree.value, path_length, ls_lens)
	return ls_lens


def test():
	assert longest_path(None) == 0
  	
	assert longest_path(Tree(1)) == 1

	assert longest_path(
		Tree(1, [
			Tree(3),
			Tree(2, [
				Tree(4)
				])
			])
		) == 2

	assert longest_path(
		Tree(5, [
			Tree(6),
			Tree(7, [
				Tree(12),
				Tree(8, [
					Tree(9, [
						Tree(10, [
							Tree(1)]),
						Tree(15)
						])
					])
				])
			])
		) == 4

	assert longest_path(
		Tree(10, [
			Tree(9),
			Tree(8, [
				Tree(12),
				Tree(7, [
					Tree(6, [
						Tree(5),
						Tree(15)
						])
					])
				])
			])
		) == 4

	assert longest_path(
  		Tree(4, [
  			Tree(5, [
  				Tree(6),
  				Tree(7, [
  					Tree(12),
  					Tree(8, [
  						Tree(9, [
  							Tree(15),
  							Tree(10)
  							])
  						])
  					])
  				])
  			])
  		) == 4

	assert longest_path(
		Tree(1, [
			Tree(3),
			Tree(2, [
				Tree(4)
				])
			])
		) == 2


if __name__ == '__main__':
	test()