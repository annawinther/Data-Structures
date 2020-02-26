# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if not self.left:
                # place our new node here
                self.left = BinarySearchTree(value)
            # otherise 
            else:
                # repeat process for the left --> turn around and 
                return self.left.insert(value)
                
        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if not self.right:
                # place one here
                self.right = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process for the right
                return self.right.insert(value)
        
        # Compare root node
            # If lesser go to left child
        # If greater or equal to go to right child
        # Else try again starting from the child on appropriate

    # if exsists then add to right: greater than or equal to --> add to right 
    # AND less than -->  add to left

    # minimum value, store values unitl we get to the None, return that value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE 
        # if target eqauls the self.value 
        if target == self.value:
            # return true
            return True


        # LEFT CASE
        # if the target is less than value
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
                
         # RIGHT CASE
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


     

   
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE 
        # if empty tree
            # return none
        
        # RECURSIVE CASE
        # if there is no right value
            # return the root node value
        # otherwise 
            # return get max of the 
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
