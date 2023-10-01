from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)
    
# put function will add an element if not already added
# or change the value of an existing element 
    def put(self, key, value):
        # check if key is smaller than the actual node
        if key < self.key:  
            # check if there is a left node
            if self.left is not None:
                # calls put function and adds key,value pair  
                self.left.put(key, value)  
            # if there is no left node (yet), key, value pair goes to right node
            else:  
            # adds left node
                self.left = Node(key, value, None, None)  
        # what if key greater than actual node
        elif key > self.key:  
            # check if right node exists
            if self.right is not None: 
                # add key, value pair 
                self.right.put(key, value)  
            # if right node does not exists
            else:  
                # add right node, key value pair
                self.right = Node(key, value, None, None)  
        # current node = value 
        else:  
            self.value = value

# returns all sorted elements as a string
    def to_string(self):
        # string that we will use to add
        result = ""  
        # is there a left node?
        if self.left is not None: 
            # add as a string, calls function 
            result += self.left.to_string()
        # add node as string 
        result += f'({self.key},{self.value}) ' 
        # check if there is a right node
        if self.right is not None:  
            # add as a string
            result += self.right.to_string()
        # returns all nodes as strings
        return result 

# this function returns the number of nodes 
    def count(self):
        count = 0
        hasLeft, hasRight = self.left is not None, self.right is not None
        if hasLeft:
            count += self.left.count()
        if hasRight:
            count += self.right.count()
        if (hasLeft and hasRight):
            count += 1
        else:
            count += 1
        return count
# return value of key 
# if key does not exists = None
    def get(self, key):
        if not self:
         return None
        # key == current node
        if self.key == key:
            # return value of current node
            return self.value
         # check if current node > key
        if self.key > key:
            # check if left node exists
            if self.left is not None:
                # returns left node key value
                return self.left.get(key)
            # right node exists?
            if self.right is not None:
                 # right node key value
                return self.right.get(key)
        if self.right is not None:
            return self.right.get(key)
        else:
            return None
# this function returns the longest direct path
    def max_depth(self):
        left=0
        right=0
        # always starts with one node
        max = 1 
        # check if there is a left Node
        if self.left is not None:  
            left += self.left.max_depth()
        # is there a right Node?
        if self.right is not None:  
            right += self.right.max_depth()
        if left < right:  
            max += right
        else: 
            max += left
        # returns max depth
        return max  

# we will use this function inside the next function
# we need it to count the number of nodes without children      
    def is_leaf(self):
        return self.right is None and self.left is None

# counts nodes with no children 
    def count_leafs(self):
        # counter starts with 0
        counter = 0
        hasLeft, hasRight = self.left is not None, self.right is not None
        # check if no children
        if self.is_leaf():
            counter += 1
        if hasLeft:
            counter += self.left.count_leafs()
        if hasRight:
            counter += self.right.count_leafs()
        # returns the variable counter 
        return counter


    # function does a left-to-right traversal order of the tree
    # get the key-value pairs sorted based on their keys
    def as_list(self, lst):
        # empty list
        lst = []  
        # node as a tuple
        tple = (self.key, self.value)
        # check if left node exists
        if self.left is not None:  
            # add left node to list as a tuple
            lst += (self.left.as_list(tple))  
        # append actual node as a tuple
        lst.append(tple)  
        # check if right node exists
        if self.right is not None:  
            # add right node to list as a tuple
            lst += (self.right.as_list(tple))
        # returns a list of tuples
        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes 
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
