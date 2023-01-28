# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer_l1 = l1
        pointer_l2 = l2
        sum_of_nums = pointer_l1.val+pointer_l2.val
        flag = int(sum_of_nums/10)
        new_digit = (sum_of_nums)%10
        new_number = ListNode(val=new_digit)
        pointer_new_number = new_number
        pointer_l1 = pointer_l1.next
        pointer_l2 = pointer_l2.next
        while True:
            if flag==0 and pointer_l1 is None and pointer_l2 is None:
                break
            sum_of_nums = flag
            if pointer_l1 is not None:
                sum_of_nums += pointer_l1.val
                pointer_l1 = pointer_l1.next
            if pointer_l2 is not None:
                sum_of_nums += pointer_l2.val
                pointer_l2 = pointer_l2.next
            new_digit = sum_of_nums%10
            flag = int(sum_of_nums/10)
            #print(f"{new_digit} - {flag}")
            pointer_new_number.next = ListNode(val=new_digit)
            pointer_new_number = pointer_new_number.next

        return new_number