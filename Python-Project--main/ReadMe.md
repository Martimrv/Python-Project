# Mini-project report 
Members: Martim Oliveira 
Program: Software Technology  
Course: 1DV501  
Date of submission: 2022-11-23

## Introduction  
    This project is part of the course Introducing to Programming - Software Technology bachelor programme. The project has 3 parts: 
    
    First part, we had to use Python´s set to count the number of unique words inside two files from assignment threee; also, we had to print the 10 most frequent words (len greater than 4) from those files too, using a dictonary. 
    
    Second part, we had to download a code skeleton, which already had a BstMap class, and we had to finish it. A BstMap is a data structure which allows the programm to look, insert and remove in a fast way. Similar to the BstMap, we also had to finish a given code skeleton based on hashing. HashSet is an unordered data structure containing unique elements in buckets. Tipically, HashSet works faster because of the hashing method to store elememts.

    Part three was divided in 4 smaller parts:
        1st - Count Unique words using HashSet implementation - we had to use the code from part1, replaced Python set´s classes for HashSet and we replaced the called functions. 
        2nd - Print a list of the top-10 most frequently used word(length > 4) - again, we used part1 code and replaced Python dictionary(counter subclass of dict, counts hashable or immutable objects) for BstMap. The program prints 10 most frequent words and how many times were used.
        3rd - Using HashSet implementation we called for ´max bucket size´ function which prints the size of the bucket with more elements; ´zero bucket ratio´ function returns the ratio between the number of buckets. 
        4th - Using BstMap implementation, we called ´count nodes´ function which returns the number of nodes of the Bst(heigh of the tree); ´max depth´ function prints the length of the tree(calculates for each node, returns the depth to the parent and compares to the left and right subtrees, returning the maximum); ´count leafs´ function returns the number of nodes without children (a leaf is a node that does´t have any children)


## Part 1: Count unique words 1
The text should include:
- How many words did each of the two text files 
``life_of_brian`` and ``swedish_news_2020`` have?
## How many words?

| File           | Total words |
|:---------------|:-----------:| 
| `brian.txt`    |    14147    |
| `swe_news.txt` |   12951518  |

- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
##  1st 
        We create a variable called "c" wich uses a dictionary subclass "counter" that stores objects as keys and counts the values. 
```python
c = Counter()
```
## 2nd
    After that, we start a for statement which will iterate each word inside the file. If the word´s len is greater than 4, the variable "c" will be incerased with 1.
```python
for w in lst:
    if len(w) > 4:
        c[w] += 1
```
## 3rd
    Then, we created a variable called "dic" which uses a Python Dictionary Method. Python Dictionary works like a ´map´ and stores data in the form of key value pair.



 - Present a unique word count and the Top-10 lists for each of the two files.
    ## Unique word count:

| File           |     Words    |
|:---------------|:------------:| 
| `brian.txt`    |    2323      |
| `swe_news.txt` |   381433     |

       
## Top-10 lists:
|    `Brian`          | - |    `Swe_news`     |
|:-----------------   |:-:|:----------------- |
|**Brian** (376)      | - |**under** (44901)  |
|**Centurion** (120)  | - |**kommer** (42017) |
|**crowd** (101)      | - |**efter** (36394)  |
|**Mother** (99)      | - |**eller** (30997)  |
|**right** (78)       | - |**ocksÃ** (30136)  |
|**Crucifixion** (73) | - |**andra** (27038)  |
|**Pilate** (73)      | - |**finns** (26759)  |
|**Pontius** (64)     | - |**sedan** (24794)  |
|**Crowd** (60)       | - |**skulle** (23450) |
|**Rogers** (52)      | - |**procent** (23420)|


## Part 2: Implementing data structures
- Give a brief presentation of the given requirements
    Part 2 we have to implement HashSet and BstMap data structure. 
    **HashSet** is a data structure that stores items using hash function to map those items. It is an unordered set and contains only unique values. The main advantage of using a hash set is that it provides constant-time performance for insert, delete and search.
    
    **BstMap** map based on binary search trees - composed of nodes, each one has a key-value pair + 2 children, left and right. 
    Values on the left are less than its own data and on the right greater than its own data. 
    If we need to search for a key, it won´t be necessary to go through all elements, thus BSTMap is fast.
    

- For the hash based word set (HashSet), present (and explain in words):
 	* Python code for function ``add``, how to compute the hash value, and rehashing.

## Ash Value:
```python      
        hash=sum(map(ord, word))%len(self.buckets)**
        return hash 
```     
    This function maps the itdems to indices in the array. It uses ord function which will return the unicode of a specified character. The map function iterates through each character of the word. The, we sum and use modulos operator of the number of buckets. 
    This function returns hash as the hash value, of a fixed length, that uniquely identifies the data. 

## Function add:
1. Adding a new word to HashSet, we need to get the word hash value

```python
    hash = self.get_hash(word)
```
2. We get the index of the bucket. The bucket holds the element using hash value

3. Is the word already in the bucket?

```python
    if word in self.buckets[hash]:
        return
```

4. After that, we add the element to the bucket

```python
    self.buckets[hash].append(word)
    self.size += 1
```

5. Finally, we call the reash function if the self.load variable is equal to 1:

```python
if self.load == 1.0: 
        self.rehash()
```

## Reashing:
    Reashing is done when the size increases more than its pre-defined; so, the size of the array increases and the values are hashed again to the doubled size array(less complex).

1. The following code, creates an empty array(double size) for the reashed values. 
```python
    new_buckets = []  
    for b in self.buckets: 
        for item in b:
            new_buckets.append(item)
```            
2. Empty buckets and for each bucket add another bucket; then, we add elements to hash again
```python
        self.buckets=[[] for i in range(len(self.buckets)*2)]
        self.size = 0
        for element in new_buckets:  
            self.add(element)
        self.load = self.size / len(self.buckets)
```

    * Point out and explain any differences from the given results in ``hash_main.py``
        When we compare the hash_output and the results from Hash_main, we notice that the order of the elements when printed isn´t exactly the same as hash_output. Theoretically, a set is an unordered collection of elements, thus the output might be accepted. Though, when we run the program the output is always the same. 


- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
## Put function:
1. First, check if `root` is `None`:
```python
    if self.root is None:
```

2. If the `root` does not exist, we add a `Node` with the key-value pair and 2 children (non-existents):
```python
self.root = Node(key, value, None, None)
```

3. If a root Node exists, we call the put method on the root:
```python
else:
    self.root.put(key, value)
```

4. Is key less than the current Node key? :

```python
    if key < self.key: 
```
5. If it is, then we check if there is a left child: 

```python
    if self.left is not None:
```

6. If left child already exists, we cal the put method on the left child and add the key-value pair:

```python
    self.left.put(key, value) 
```
If there is no left child, we add a left child with the key-value pair and 2 children(None, None):

```python
else:  
    self.left = Node(key, value, None, None)  
```

7. If the key is greater than the current Node, we repeat the same process:

```python
 elif key > self.key:  
    # check if right node exists
    if self.right is not None: 
        # add key, value pair 
        self.right.put(key, value)  
    # if right node does not exists
    else:  
        # add right node, key value pair
        self.right = Node(key, value, None, None)
```
8. If the key is equal to the current Node:
```python
else:  
    self.value = value
```

## Max_depth function:
    The maximum depth of a binary search tree(BST) is the maximum number of nodes form the root node to the deepest leaf node in the tree. It is important to keep the maximum depth of a BST as small as possible, it can affect the performance of operations. 
    Generally, the max depth is an important aspect when we want to evaluate the performance and efficiency of a BST. A well-balanced BST with a small max depth provides a faster search and insertion. 

1. First, we check if the root exists. If the root is None, it returns zero.

```python
    if self.root is None:
        return 0
```
2. If the root Node exists it calls the `max_depth` on the root:

```python
else:
    return self.root.max_depth()
```

3. Node starts with `max` == 1 and no left or right depth. After that, checks if `left-Node` exists and increments left variable: 

```python
if self.left is not None:  
            left += self.left.max_depth()
```

4. Repeats the same for `right-Node`:
```python
if self.right is not None:  
    right += self.right.max_depth()
```

5. Finally, compares left and right and increments with the biggest:

```python
if left < right:  
    max += right
else: 
    max += left
    # returns max depth
return max  
```


* Point out and explain any differences from the given results in ``bst_main.py``.
When I run the program there are no differences from the given results. 


## Part 3: Count unique words 2

Part 3 we had to repeat the code from Part 1, though, in place of using a `set` and a `dictionary` to count unique words and 10 most frequent words, I used the `BstMap`and `HashSet` data structure that I have created.
```python
    unique_words = hashSet.HashSet()
    all_words=bstMap.BstMap()
```
## Top-10 implementation
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.

1. After we call the `BstMap` for all words inside the files, we iterate each word inside all_words:               
```python
   for each_word in lst:
        if len(each_word) > 4:
            found=all_words.get(each_word)
```
We check if the len of each word is greater than 4 and we get the value of the current word inside `BstMap`. 

2. Then, we check if the variable `found` is not none; if there are occurrences, we increase the found value with one.

```python
if found is not None:
        add_node=found + 1
        all_words.put(each_word, add_node)
```

3. If it is None, there are occurrences; we `put` the word with the value of 1.

```python
else:
    all_words.put(each_word,1)
```

4. Created a variable which has a sorted list:

```python
        words_list=all_words.as_list()
```

5. The next variable sorts each word by its  `value`, in reversed order, in order to the most used words appear first:

```python
sorted_words_list = sorted(words_list, key=operator.itemgetter(1), reverse=True)
```

6. `i` works as a counter; we just want to present the  `Top-10`; 
    Then, we add to the variable  `result` the first most frequent word and the number of times this word was repeated:

```python
i=0
    result=""
    while i < 10 and i < len(sorted_words_list):
            result += f'{i+1} - "{sorted_words_list[i][0]}" used {sorted_words_list[i][1]} times.\n'
            i += 1
```
 
- Present a unique word count and the Top-10 lists for each of the two files.
## Number of Unique words:

|`brian`       | - | `Swe_news` |
|:-------------|:-:|:-----------|
|2323 words    | - |381433 words|

    
## Top-10 most used words:

|    `Brian`          | - |    `Swe_news`     |
|:-----------------   |:-:|:----------------- |
|**Brian** (376)      | - |**under** (44901)  |
|**Centurion** (120)  | - |**kommer** (42017) |
|**crowd** (101)      | - |**efter** (36394)  |
|**Mother** (99)      | - |**eller** (30997)  |
|**right** (78)       | - |**ocksÃ** (30136)  |
|**Crucifixion** (73) | - |**andra** (27038)  |
|**Pilate** (73)      | - |**finns** (26759)  |
|**Pontius** (64)     | - |**sedan** (24794)  |
|**Crowd** (60)       | - |**skulle** (23450) |
|**Rogers** (52)      | - |**procent** (23420)|

       
* What is the bucket list size, max bucket size and zero bucket ratio for HashSet, and the total node count, max depth and leaf count for BstMap, after having added all the words in the two large word files? (Hence, eight different numbers.)

| File             |  Bucket list size |  Max bucket |  Zero bucket ratio | Total Node count | Max depth| Leaf count|
|:-----------------|:-----------------:|:-----------:|:------------------:|:----------------:|:--------:|:---------:|
| `brian`          |        4096       |      17     |       1.45         |      1526        |    28    |    494    |
| `swe_news`       |       524288      |     645     |       1.37         |     361342       |   103    | 116935    |


* Explain how max bucket size and zero bucket ratio can be used to evaluate the quality of your hash function in HashSet. What are optimal/reasonable/poor values in both cases?
    An ideal implementation will use a hash function that distributes evenly among all buckets in order to have as few records as possible to store in the overflow bucket.
    From our perspective, we think that a good hash function will distribute the values through the buckets, trying to have the smallest amount of values inside overflow bucket(infinite capacity).
    The maximum bucket size of a hash set depends on the implementation of the hash set. In general, a hash set uses an array to store the elements, and each element is stored in a "bucket" in the array. The maximum size of the bucket is determined by the size of the array and the number of elements that the hash set can store.
    For example, if the hash set is implemented using an array with a capacity of 10, and each bucket can store a maximum of 2 elements, then the maximum bucket size of the hash set would be 2.
    If the maximum bucket size of a hash set is too small, it can lead to poor performance. This is because a small bucket size can result in a large number of collisions, which occur when two or more elements are mapped to the same bucket. One way to reduce collisions is to increase the maximum bucket size, which can be done by increasing the size of the array or using a different hash function that maps elements to different buckets more evenly. However, increasing the maximum bucket size can lead to increased memory usage and longer searching times, if the bucket size becomes too large.
    The bucket ratio of a hash set is a measure of how full the hash set is. A zero bucket ratio means that there are no elements in the hash set, or that all the elements are mapped to a single bucket. This could be the result of a poorly designed hash function that always maps all the elements to the same bucket. Generally, it is not desirable to have a Zero Bucket Ratio as it can lead to poor performance, because a single bucket must store all the elements, which can result in a large bucket size and increased collision rates. 


* Explain how max depth and leaf count can be used to evaluate the efficiency of the BstMap. What are optimal/reasonable/poor values in both cases?
    The maximum depth of a BST is the length of the longest path from the root of the tree to a leaf node. The quality of the BST can be evaluated based on how well balanced the tree is, which we can determined in part by its max depth. 
    A well-balenced BST has a small max depth, which shows that the tree is not overly skewed in a particular direction. This leads to a better overall performance, as well as faster search and insertion times. Generally, the balance of the BST is important in order to ensure a good performance and efficiency. 
    Regarding the leaf count, it is the number of nodes in the tree that have no children. Leaf count can be considered a good indicator of how well balanced the BST is.
    A well-balanced BST should have a leaf count that is close to the maximum possible for a tree of its height. A perfectly balanced BST with a height of 3 should have a leaf count of 4. 
    However, if the leaf count is smaller than the maximum possible for a tree of its height, it indicates that the tree is not well-balanced, which can lead to slower search and insertion times. A leaf count much larger can indicate that the tree is over-full. 


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming?
    From our perspective, conclude hashset(code skeletons) and implement hashinh and Bst in part 3.
    Hashing is a complex topic and it was hard to understand and create the solutions for the programmes.
- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
    We should have organised the tasks ans stick to it.
- How could the results be improved if you were given a bit more time to complete the task.
    More commits with smaller steps and work equally divided.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
    We communicate with a whatsapp group.
- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.
  ## Members tasks:
        Martim Oliveira: part 1 function read file + count unique words + previous functions; 
                         BstMap and part of Hashset
                         Part 3 Read file function + unique words + previous functions;
                         ReadMe file
    
 	* Estimate hours spend each week (on average)
        On average, 6 hours per weak
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.
        Divide the work per tasks and add deadlines to finish it, is always the best approach;
        Follow the work of all the colleagues;
        Create a deadline in advance of the professor´s(5 days before the offical deadline);





    



