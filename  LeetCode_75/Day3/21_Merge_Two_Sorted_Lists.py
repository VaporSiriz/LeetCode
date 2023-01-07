from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next
    
    def __iter__(self):
        node = self
        while node is not None:
            print(f"node : {node}")
            yield node.val
            node = node.next

def mergeTwoLists(
    list1: Optional[ListNode],
    list2: Optional[ListNode]
) -> Optional[ListNode]:

    # 하나라도 None이면 반대 list를 반환
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    pointer_1 = list1
    pointer_2 = list2
    result = ListNode()

    if list1.val <= list2.val:
        result.val = list1.val
        pointer_1 = pointer_1.next
    else:
        result.val = list2.val
        pointer_2 = pointer_2.next

    pointer_result = result
    while pointer_1 is not None and pointer_2 is not None:

        new_node = ListNode()
        if pointer_1.val <= pointer_2.val:
            new_node.val = pointer_1.val
            pointer_1 = pointer_1.next
        else:
            new_node.val = pointer_2.val
            pointer_2 = pointer_2.next
        pointer_result.next = new_node
        pointer_result = pointer_result.next

    while pointer_1 is not None:
        new_node = ListNode(val=pointer_1.val)
        pointer_result.next = new_node
        pointer_result = pointer_result.next
        pointer_1 = pointer_1.next

    while pointer_2 is not None:
        new_node = ListNode(val=pointer_2.val)
        pointer_result.next = new_node
        pointer_result = pointer_result.next
        pointer_2 = pointer_2.next

    return result

# list1 = ListNode(val=1)
# list1.next = ListNode(val=2)
# list1.next.next = ListNode(val=4)

# list2 = ListNode(val=1)
# list2.next = ListNode(val=3)
# list2.next.next = ListNode(val=4)
list2 = ListNode()

merged_list = mergeTwoLists(None, list2)
iter_list = iter(merged_list)
for element in iter_list:
    print(element)
