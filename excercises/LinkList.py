
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next


llist = LinkList()
llist.append(6)
llist.push(7)
llist.push(1)
llist.append(4)
llist.insertAfter(llist.head.next,8)
llist.printlist()
