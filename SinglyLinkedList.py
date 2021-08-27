"""
Definition for singly-linked list
class ListNode:
    def __init__(self, val):
    self.val = val
    self.next = None
"""
from ListNode import ListNode


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the LL. If invalid, return -1
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of val before the index-th node in the LL
        If index == LL length, append to the end of the LL
        If index > LL length, do not insert
        """
        if index < 0:
            index = 0

        if index >= self.size:
            return

        node = ListNode(val)

        if index == 0:
            node.next = self.head
            head = node
            self.size += 1
            return

        cur = self.head
        for i in range(1, index):
            cur = cur.next

        node.next = cur.next
        cur.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        cur = self.head
        for i in range(1, index):
            cur = cur.next
        # cur is now at the node before the index-th
        cur.next = cur.next.next
        self.size -= 1

    def printAll(self):
        cur = self.head
        for i in range(self.size):
            print(cur.val)
            cur = cur.next

myLinkedList = SinglyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
myLinkedList.printAll()
myLinkedList.get(1)              # return 2
myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
myLinkedList.get(1)           # return 3
myLinkedList.printAll()
