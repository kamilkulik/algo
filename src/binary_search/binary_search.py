# the input array needs to be sorted
# the iterative approach

def binarySearch(array, target):
	# 1. Pass into helper function two pointers - left and right to keep track of current bounds
	return binary_search_helper(array, target, left = 0, right = len(array) - 1)

def binary_search_helper(array, target, left, right):
	# 2. Loop over the array while left pointer is less or equal right pointer
	while left <= right:
		# 3. Determine the index of middle number in the array
		middle = (right + left) // 2 # // returns quotient as integer (rounded down)
		# 4. Check if middle of array is equal to the target value
		if array[middle] == target:
			return middle
		# 5. if determined middle is greater than target, we need to look at the array to the left of the middle (excluding it)
		elif array[middle] > target:
			# we move the right pointer to the left excluding the middle index
			right = middle - 1 # -1 is used to exlcude the element at the middle pointer
		# 6. do the opposite to point 5
		elif array[middle] < target:
			left = middle + 1
	return -1 # in case such number wasn't found the array

# RECURSIVE SOLUTION

def binarySearchRecursive(array, target):
	left = 0
	right = len(array) -1

	return binarySearchRecursiveHelper(array, target, left, right)

def binarySearchRecursiveHelper(array, target, left, right):

	if left > right: return -1

	middle = (left + right) // 2
	
	if array[middle] == target:
		return middle
	elif array[middle] > target:
		right = middle - 1
		return binarySearchRecursiveHelper(array, target, left, right)
	elif array[middle] < target:
		left = middle + 1
		return binarySearchRecursiveHelper(array, target, left, right)