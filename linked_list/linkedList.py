# Credit for this code goes to Sadrach Pierre, Ph.D.
# https://towardsdatascience.com/linked-lists-in-python-91906f22a282


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def printLL(self):
        value = self.head
        while (value):
            print(value.data)
            value = value.next


if __name__ == "__main__":
    # init linked list
    ll = LinkedList()
    # assign values
    ll.head = Node("Speak to me")
    second = Node("Breathe")
    third = Node("On the Run")
    fourth = Node("Time")
    fifth = Node("The Great Gig in the Sky")
    # link items
    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # print linked list
    ll.printLL()
