list_for_in_place_reversal = [4, 5, 6, 7, 9, 11, 435, 45, 1]

def reverse_list_in_place(list):
	start = 0
	end = len(list) - 1

	while start < end:
		list[start], list[end] = list[end], list[start]
		start += 1
		end -= 1

reverse_list_in_place(list_for_in_place_reversal)
print(list_for_in_place_reversal)


def reverse_list_recursively(list):
	if len(list) == 0: return []

	return [list[-1]] + reverse_list_recursively(list[: -1])


print(reverse_list_recursively([4, 5, 6, 7, 9, 11, 435, 45, 1]))



reverse_lambda_recursion = lambda list: (reverse_lambda_recursion(list[1:]) + list[:1] if list else [])

print(reverse_lambda_recursion([4, 5, 6, 7, 9, 11, 435, 45, 1]))