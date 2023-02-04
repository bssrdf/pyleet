# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def constructList(items):
    node = ListNode(0)
    head = node
    for i in items:
        node.next = ListNode(i)
        node = node.next
    return head.next  

def printList(head):
    while head:
        print(str(head.val)+'->',end='')
        head = head.next
    print('null')

if __name__ == "__main__":
     head = constructList([1, 2, 3, 3, 4, 4, 5])    
     printList(head)