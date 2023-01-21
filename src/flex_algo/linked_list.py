class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        return '->'.join(str(n) for n in nodes)

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def push_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node

    def reverse(self):
        curr = self.head
        pre, nxt = None, None

        while curr is not None:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        self.head = pre

    def reverse_between(self, start, end):
        curr = self.head
        pre_start = curr
        idx = 0

        # find the start node
        while idx < start - 1:
            pre_start = curr
            curr = curr.next
            idx += 1

        start_node = curr

        pre, nxt = None, None
        while idx < end and curr is not None:
            idx += 1
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        pre_start.next = pre
        start_node.next = curr


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


if __name__ == '__main__':
    print('=============testing Linked List==========')
    node_a = Node('a')
    print(node_a)

    llist = LinkedList()

    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    llist.push_back(5)
    print(llist)

    llist.reverse_between(2, 4)
    print(llist)

    llist2 = LinkedList()
    llist2.push_back(5)
    llist2.reverse_between(1, 1)
    print(llist2)


