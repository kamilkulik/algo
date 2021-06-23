def reverse_list_in_place(list):
	start = 0
	end = len(list) - 1

	while start < end:
		list[start], list[end] = list[end], list[start]
		start += 1
		end -= 1

	return list

print(reverse_list_in_place([4, 5, 6, 7, 9, 11, 435, 45, 1]))



def reverse_list_in_place_recursively(list):
	if len(list) == 0: return []

	return [list[-1]] + reverse_list_in_place_recursively(list[: -1])


print(reverse_list_in_place_recursively([4, 5, 6, 7, 9, 11, 435, 45, 1]))



reverse_list_in_place_lambda = lambda list: (reverse_list_in_place_lambda(list[1:]) + list[:1] if list else [])

print(reverse_list_in_place_lambda([4, 5, 6, 7, 9, 11, 435, 45, 1]))