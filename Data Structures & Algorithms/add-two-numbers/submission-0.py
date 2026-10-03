# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):, final
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseLL(linkylist):
            curr = linkylist
            prev = None
            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev

        def totalSum(linkylist):
            curr = linkylist
            total = ""
            while curr != None:
                total += str(curr.val)
                curr = curr.next

            return total


        def backToLinkedList(finalSum):

            head = None
            curr = None
            finalStr = str(finalSum)
            for char in finalStr[::-1]:
                newNode = ListNode(int(char))

                if head is None:
                    head = newNode
                    curr = newNode
                else:
                    curr.next = newNode
                    curr = newNode
        
            return head

        rl1 = reverseLL(l1)
        rl2 = reverseLL(l2)

        t1 = int(totalSum(rl1))
        t2 = int(totalSum(rl2))

        finalSum = t1 + t2
        
        return backToLinkedList(finalSum)

