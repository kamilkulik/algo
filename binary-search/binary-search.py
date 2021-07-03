# the input array needs to be sorted
# the iterative approach

def binarySearch(array, target):
	# initilise two pointers - left and right to keep track of current bounds
	left = 0
	right = len(array) - 1

	while left <= right:
		middle = (right + left) // 2 # determine the index of middle number in the array

		if array[middle] == target:
			return middle
		elif array[middle] > target:
			# we move the right pointer to the left excluding the middle index
			right = middle - 1
		elif array[middle] < target:
			left = middle + 1
	return -1 # in case such number wasn't found the array

print(binarySearch([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 26))
print(binarySearch([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 68))

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

print(binarySearchRecursive([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 26))
print(binarySearchRecursive([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 68))