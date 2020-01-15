class ListNode():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def reverseList(self,head):
        if head != None:
            current_node = head.next
            prv_node = head
            while current_node != None:
                next_node = current_node.next
                current_node.next = prv_node
                prv_node = current_node
                current_node = next_node
            head.next = None
            head = prv_node
        return head


    


def main():
   pass




if __name__ == '__main__':main()
