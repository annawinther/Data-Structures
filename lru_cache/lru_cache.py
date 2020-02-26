from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # checking if key is in our storage and setting a node to be the key (accessing the key directly, O(1))
        # moving the key to the end and returning the value of the key of that node
        if key in self.storage:
            node = self.storage[key]
            self.cache.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # create node if key is not found and move to front
        # move node to end if key is found
        # if key is found, update it and move to the end ( most recently used )
        # if its full remove the last node from linked list and dictionary
        # tail is most recently used and head is the least recently used

        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.cache.move_to_end(node)
            return

        if self.size == self.limit:
            del self.storage[self.cache.head.value[0]]
            self.cache.remove_from_head()
            self.size -= 1

        self.cache.add_to_tail((key, value))
        self.storage[key] = self.cache.tail
        self.size += 1
  



