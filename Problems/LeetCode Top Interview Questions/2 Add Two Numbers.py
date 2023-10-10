# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # this solution beats 29% speed and 77% memory
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ''
        carry = 0

        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
                

            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
                
            val = val1 + val2 + carry

            if val >= 10:
                val = val % 10
                carry = 1
            else:
                carry = 0

            result += str(val)
        
        if carry == 1:
            result += '1'

        result = result[::-1]

        node = ListNode(result[0])

        for i in range(1, len(result)):
            node = ListNode(result[i], node)
        
        return node
    
    # speed same, very slightly less memory usage

    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     carry = 0
    #     count = 0
    #     first_node = ListNode(0)
    #     while l1 or l2:
    #         if l1:
    #             val1 = l1.val
    #             l1 = l1.next
    #         else:
    #             val1 = 0
                

    #         if l2:
    #             val2 = l2.val
    #             l2 = l2.next
    #         else:
    #             val2 = 0
                
    #         val = val1 + val2 + carry

    #         if val >= 10:
    #             val = val % 10
    #             carry = 1
    #         else:
    #             carry = 0

    #         if count == 0:
    #             first_node = ListNode(val)
    #             count += 1
    #         elif count == 1:
    #             node = ListNode(val)
    #             first_node.next = node
    #             prev_node = node
    #             count += 1
    #         else:
    #             node = ListNode(val)
    #             prev_node.next = node
    #             prev_node = node
        
    #     if carry == 1:
    #         node = ListNode(1)
    #         if first_node.next:
    #             prev_node.next = node
    #         else:
    #             first_node.next = node
    #     return first_node