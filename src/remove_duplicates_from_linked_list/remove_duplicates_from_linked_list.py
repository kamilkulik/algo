class Linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None

# Solution 1
# iterate over every node of the linekd list and remove duplicates one by one
# O(n) time and O(1) space

def removeDuplicatesFromLinkedList_separately(linkedList):
	prev = None
	curr = linkedList
	
	while curr is not None:
		if prev and curr.value == prev.value:
			prev.next = curr.next
			curr = curr.next
			
		else:
			prev = curr
			curr = curr.next
			
	return linkedList

# Solution 2
# iterate over nodes, when next node's value is same as current node's, loop over subsequent node to find the first unique one and so on
# O(n) time and O(1) space

def removeDuplicatesFromLinkedList(linked_list):
    # 1. We need to keep track of the first unique node - be default it will be the first node we pass into the function
    current_node = linked_list
	# 2. We then use a while loop which will exit when current_node is None
    while current_node is not None:
        # 3. We use a look ahead approach. Let's initiate a variable to hold our next_unique_value.
        # the plan is to check each value if it's unique compared to current_node's value
        # and move on to the next node in case of value duplication
        next_unique_node = current_node.next
        # 4. We do a second while loop which will exit only when the next node has unique value
        while next_unique_node is not None and current_node.value == next_unique_node.value:
            # 5. Assign next_unique_node to the next node (because the while loop fired which means a duplicate was found)
            next_unique_node = next_unique_node.next
        # 6. outside of second while loop, reassign current_node's next value to the next_unique node
        # if the subsequent node was unique, we'll reassign the same node
        # if node wasn't unique we'll assign the next unique node
        current_node.next = next_unique_node
        # 7. now we need to reassign the current node so the while loop can continue
        current_node = next_unique_node
        
    return linked_list
