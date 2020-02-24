from doubly_linked_list import DoublyLinkedList
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
    def enqueue(self, value):
        self.size += 1
        print(value)
        self.storage.add_to_tail(value)
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            # value = self.storage.remove_from_head()
            return None
            # print('value', value)
    def len(self):
        return len(self.storage)