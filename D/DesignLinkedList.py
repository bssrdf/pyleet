'''

-Medium-


Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.


'''
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        cur, i = self.head, 0
        while cur and i < index:
            cur = cur.next
            i += 1
        return cur.val if cur else -1
           
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node        

    def addAtTail(self, val: int) -> None:
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)    
        else:
            self.head = Node(val)    


        

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(-1)
        dummy.next = self.head
        cur, i = self.head, 0
        prev = dummy
        while cur and i < index:
            prev = cur
            cur = cur.next
            i += 1
        if i == index:
            node = Node(val)
            prev.next = node
            node.next = cur
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(-1)
        dummy.next = self.head
        cur, i = self.head, 0
        prev = dummy
        while cur and i < index:
            prev = cur
            cur = cur.next
            i += 1
        if cur:            
            prev.next = cur.next
        self.head = dummy.next

if __name__ == "__main__":
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
    print(myLinkedList.get(1))              # return 2
    myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
    print(myLinkedList.get(1))              # return 3
    myLinkedList = MyLinkedList()
    myLinkedList.addAtTail(3)
    print(myLinkedList.get(0))              # return 3
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(2)
    myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
    myLinkedList.addAtHead(2)
    myLinkedList.addAtHead(7)
    myLinkedList.addAtHead(3)
    myLinkedList.addAtHead(2)
    myLinkedList.addAtHead(5)
    myLinkedList.addAtTail(5)
    print(myLinkedList.get(5))              # return 3
    myLinkedList.deleteAtIndex(6)    # now the linked list is 1->3
    myLinkedList.deleteAtIndex(4)    # now the linked list is 1->3





        