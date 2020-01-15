class LinkedList():
    def mergeTwoLists(self,l1,l2):
        head = l1 if l1.val < l2 else l2
        l1_current = l1
        l2_current = l2
        while l1_current != None and l2_current != None:
            if l1.val < l2.val:
                l1_current = l1.next
                l1.next = l2
            else:
                l2_current = l2.next
                l2.next = l1

        return head
            