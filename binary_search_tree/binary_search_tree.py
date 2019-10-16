import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to the right child node
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if the new nodes value is less than our current ones value
        if value < self.value:
            # if the is no left child,
            if self.left != None: 
                # place a new node here
                self.left.insert(value)
            # otherwise
            else:
                # repeat process for left
                self.left = BinarySearchTree(value)
        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current parent value
        elif value > self.value:
            # if there is no right child here,
            if self.right != None: 
                # place a new one
                self.right.insert(value)
            # otherwise
            else:
                # repeat process right
                self.right = BinarySearchTree(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        if self.value == target:
          return True
        # LEFT CASE
        elif self.value > target:
          if self.left == None:
            return False
          return self.left.contains(target)
        # RIGHT CASE
        else: #(if self.value < target)
          if self.right == None:
            return False
          return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE 
        # if empty tree
        if self.value == None:
            # return none
            return None
        
        # RECURSIVE
        # if the the is no right value
        # if 
            # return the root value
        # return the get max of the the right node

        # ITTERATIVE
        # set a max value variable to keep track of max value
        # get a ref to current node
        # check if we are at a valid tree node
            # if our current value is greater than the max value
                # update the max value
            # move on to the next right node in the tree
            # setting the current node to the current nodes right
        # return our max value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # base case

        # left case

        # right case
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

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
