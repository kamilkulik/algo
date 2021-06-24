class LinkedList:
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
    current_node = linked_list
	
    while current_node is not None:
        next_unique_node = current_node.next
        
        while next_unique_node is not None and current_node.value == next_unique_node.value:
          next_unique_node = next_unique_node.next
        
        current_node.next = next_unique_node
        current_node = next_unique_node
        
        
    return linked_list

