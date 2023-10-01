from dataclasses import dataclass
from typing import List
from fractions import Fraction


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.load = 0
        self.key_range = 8
        self.buckets = [[] for item in range(self.key_range)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash=sum(map(ord, word))%len(self.buckets)
        return hash

     # Adds a word to set if not already added
    def add(self, word):
        hash = self.get_hash(word)
        if word in self.buckets[hash]:
            return
        self.buckets[hash].append(word)
        self.size += 1 
        self.load = self.size / len(self.buckets)
        if self.load == 1.0: 
            self.rehash()

    # Doubles size of bucket list
    def rehash(self):
        new_buckets = []  
        for b in self.buckets: 
            for item in b:
                new_buckets.append(item)
        self.buckets=[[] for i in range(len(self.buckets)*2)]
        self.size = 0
        for element in new_buckets:  
            self.add(element)
        self.load = self.size / len(self.buckets)

    # Returns a string representation of the set content
    def to_string(self):
        text=" "
        for b in range(0, len(self.buckets)): 
            for item in self.buckets[b]:
                text += '{0} '.format(item)
        return '{' + text + '}'

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hash = self.get_hash(word)
        if word in self.buckets[hash]:  
            return True  
        return False 

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        hash = self.get_hash(word)
        b = self.buckets[hash]
        if self.contains(word):
            b.remove(word)
            self.size-=1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        sum_size = 0  
        for b in self.buckets: 
           if len(b) > sum_size: 
                sum_size = len(b) 
        return sum_size

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        sum_zero_buckets = 0 
        for b in self.buckets: 
            b_length=len(b)
            if b_length == 0:
                sum_zero_buckets += 1
        ratio=sum_zero_buckets/(self.size-1)
        return ratio
