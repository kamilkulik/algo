from src.remove_duplicates_from_linked_list.remove_duplicates_from_linked_list import removeDuplicatesFromLinkedList_separately
from src.remove_duplicates_from_linked_list.remove_duplicates_from_linked_list import removeDuplicatesFromLinkedList
from src.linked_list.linked_list import Linked_list

def build_linked_list(list):
    head = list[0]
    nodes = list[1:]
    linked_list = Linked_list(head)
    curr_node = linked_list
    for node in nodes:
        curr_node.insert(node)
        curr_node = curr_node.next
    return linked_list

def test_remove_duplicates_from_linked_list_1():
    list = [ 1, 1, 1, 3, 4, 4, 4, 5, 6, 6 ]
    result = [ 1, 3, 4, 5, 6 ]

    og_list = build_linked_list(list)
    unique_items_list = build_linked_list(result)
    
    cleaned_list = removeDuplicatesFromLinkedList_separately(og_list)

    curr_cleaned_node = cleaned_list
    curr_unique_node = unique_items_list
    while curr_cleaned_node is not None:
        assert curr_cleaned_node.value == curr_unique_node.value
        curr_cleaned_node = curr_cleaned_node.next
        curr_unique_node = curr_unique_node.next

def test_removeDuplicatesFromLinkedList_1():
    list = [ 1, 1, 1, 3, 4, 4, 4, 5, 6, 6 ]
    result = [ 1, 3, 4, 5, 6 ]

    og_list = build_linked_list(list)
    unique_items_list = build_linked_list(result)
    cleaned_list = removeDuplicatesFromLinkedList(og_list)

    curr_cleaned_node = cleaned_list
    curr_unique_node = unique_items_list
    while curr_cleaned_node is not None:
        assert curr_cleaned_node.value == curr_unique_node.value
        curr_cleaned_node = curr_cleaned_node.next
        curr_unique_node = curr_unique_node.next