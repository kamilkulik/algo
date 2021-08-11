# Perfect problem to discuss space and time optimisation

# better time complexity solution
# hash table based:

# time: O(n), space O(n)

def two_num_sum(array, target):
	memory = {}

	for n in array:
		potential_num = target - n
        
		if n in memory: 
			return [potential_num, n]
		else:
			memory[potential_num] = True
	
	return []

# pointer based solution
# time: O(log(n)), space: O(1)

def two_num_sum_pointer(array, target):
	array.sort()
	pointer_left = 0
	pointer_right = len(array) - 1
	
	while pointer_left < pointer_right:
		current_left = array[pointer_left]
		current_right = array[pointer_right]
		current_sum = current_left + current_right

		if current_sum == target:
			return [current_left, current_right]
		elif current_sum < target:
			pointer_left += 1
		elif current_sum > target:
			pointer_right -= 1
	
	return []