def remove_kth_from_end(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    # head node
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    # other nodes
    # first move both pointers till the end
    # second will become None
    while second.next is not None:
        first = first.next
        second = second.next
    # first should be point now to the node
    # BEFORE the k-th node from end
    # which is the node for removal
    first.next = first.next.next
    return head
