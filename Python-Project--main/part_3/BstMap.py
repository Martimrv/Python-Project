from collections import Counter
from dataclasses import dataclass
from itertools import count
from operator import countOf
from queue import Empty, Queue
from typing import Any, Optional
from xml.etree.ElementTree import tostring

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
    hd = 0
    

    def put(self, key, value):
        if self.key == key:
            temp=self
            self.value=value
            self.left=temp.left
            self.right=temp.right
            return True
        elif self.key > key:
            if self.left:
                return self.left.put(key, value)
            else:
                self.left=Node(key, value)
                return True
        elif self.key < key:
            if self.right:
                return self.right.put(key, value)
            else:
                self.right=Node(key,value)
                return True
        else:
            self=Node(key,value)
            return True
        

    def to_string(self):
        result=""
        dic=dict()
        stack = [self]
        node = None
        while stack:
            if node is None:
                node = stack.pop()
            if node is not None:
                dic[node.key]=node.value
                stack.append(node.right)
                node = node.left
        for key in dic:
            result+= "(" +str(key) + "," + str(dic[key]) + ") "
        return result
        

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

   

    def get(self,key):
        if not self:
         return None
        if self.key == key:
            return self.value
        if self.key > key:
            if self.left is not None:
                return self.left.get(key)
            if self.right is not None:
                return self.right.get(key)
        if self.right is not None:
            return self.right.get(key)
        else:
            return None
    
    def max_depth(self):
        
        def getmaxDepth(node):
            if not node:
                return 0
            
            left = getmaxDepth(node.left)
            right = getmaxDepth(node.right)
            
            return 1 + max(left, right)
        
        return getmaxDepth(self)


    def is_leaf(self):
        return self.right is None and self.left is None

    def is_node(self):
        return self.right is None or self.left is None

    def count_leafs(self):
        counter = 0
        hasLeft, hasRight = self.left is not None, self.right is not None
        if self.is_leaf():
            counter += 1
        if hasLeft:
            counter += self.left.count_leafs()
        if hasRight:
            counter += self.right.count_leafs()
        return counter
    

    def count_nodes(self):
        count = 1
        if self.left:
            count += self.left.count_nodes()
        if self.right:
            count += self.right.count_nodes()
        return count

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst): 
        stack = [self]
        node = None
        while stack:
            if node is None:
                node = stack.pop()
            if node is not None:
                lst.append((node.key, node.value))
                stack.append(node.right)
                node = node.left
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
    

    def printTree(self):
        if self.root is None:     # Empty, return empty brackets
            return ""
        else:
            return self.root.printTree()

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    def count_nodes(self):
        return self.root.count_nodes()

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
