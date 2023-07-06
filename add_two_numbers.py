# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummyHead is only used as a pointer to the built list
        # the value is not actually used thus it's set to 0
        # that's also why at the end you return dummyHead.next instead
        # of dummyHead
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        # while l1 is still looping
        # while l2 is still looping
        # while the carry still has a non-zero value continue
        # this ensures the calculation is complete
        while l1 != None or l2 != None or carry != 0:
            # fetch the curr value from l1, l2 otherwise set a 0 in
            # the column
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            
            # do the basic addition, including the carry value
            # from previous iteration
            columnSum = l1Val + l2Val + carry
            
            # the carry is found by stripping out the tens, this is used in the NEXT iteration until carry == 0
            carry = columnSum // 10
            
            # create a new node and set the node to a single digit
            newNode = ListNode(columnSum % 10)

            # add the node to the linked list
            curr.next = newNode
            # advance the list we are building (the return list)
            curr = newNode
            # advance the existing lists that came in as args
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # return the "true" head of the list
        return dummyHead.next
        
    
