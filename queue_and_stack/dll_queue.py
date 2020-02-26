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
        # runtime complexity is O(1)
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

if __name__ == '__main__':
        q = Queue()
        q.enqueue(100)
        q.enqueue(101)
        q.enqueue(105)
        print(f'dequeue should return 100: {q.dequeue()}') # => 100
        print(f'Len should return 2: {q.len()}') # => 2
        print(f'dequeue should return 101: {q.dequeue()}') # => 101
        print(f'Len should return 1: {q.len()}') # =>  1
        print(f'dequeue should return 105: {q.dequeue()}') # => 105
        print(f'Len should return 0: {q.len()}') # =>  0
        print(f'dequeue should return None: {q.dequeue()}') # => None
        print(f'Len should return 0: {q.len()}') # => 0
        
# import unittest
# class QueueTests(unittest.TestCase):
#     def setUp(self):
#         self.q = Queue()

#     def test_len_returns_0_for_empty_queue(self):
#         self.assertEqual(self.q.len(), 0)

#     def test_len_returns_correct_length_after_enqueue(self):
#         self.assertEqual(self.q.len(), 0)
#         self.q.enqueue(2)
#         self.assertEqual(self.q.len(), 1)
#         self.q.enqueue(4)
#         self.assertEqual(self.q.len(), 2)
#         self.q.enqueue(6)
#         self.q.enqueue(8)
#         self.q.enqueue(10)
#         self.q.enqueue(12)
#         self.q.enqueue(14)
#         self.q.enqueue(16)
#         self.q.enqueue(18)
#         self.assertEqual(self.q.len(), 9)

#     def test_empty_dequeue(self):
#         self.assertIsNone(self.q.dequeue())
#         self.assertEqual(self.q.len(), 0)

#     def test_dequeue_respects_order(self):
#         self.q.enqueue(100)
#         self.q.enqueue(101)
#         self.q.enqueue(105)
#         self.assertEqual(self.q.dequeue(), 100)
#         self.assertEqual(self.q.len(), 2)
#         self.assertEqual(self.q.dequeue(), 101)
#         self.assertEqual(self.q.len(), 1)
#         self.assertEqual(self.q.dequeue(), 105)
#         self.assertEqual(self.q.len(), 0)
#         self.assertIsNone(self.q.dequeue())
#         self.assertEqual(self.q.len(), 0)

# if __name__ == '__main__':
#     unittest.main()


        
