import unittest
from flex_algo import linked_list

class MyTestCase(unittest.TestCase):
    def test_reverse_between(self):
        llist = linked_list.LinkedList()
        llist.push_back(5)
        llist.reverse_between(1, 1)
        print(llist)


if __name__ == '__main__':
    unittest.main()
