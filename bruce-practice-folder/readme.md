**Reverse Linked List:** 
The iterative solution utilizes multiple O(1) rewriting moves, and since we pass through the entire array, we require O(n) time and constant space overhead (since we only need to maintain three pointers, curr, prev and next at all times throughout our entire algorithm). 

<img width="728" alt="image" src="https://user-images.githubusercontent.com/49863684/191891691-dc2c2c18-b4c3-494b-a51f-f430e2c4c410.png">

The recursive solution is easier to reason about, but requires more computational/space overhead O(n) compared to the iterative solution (since we need to create n stack frames throughout our recursion), we can re-wire the first node of our linked list, and subsequently recursively call our Reverse() function on the remainder of the linked list. 

**Reverse Node in k-group:** Given a linked list, reverse the elements in the linked list in groups of k at a time. 

<img width="740" alt="image" src="https://user-images.githubusercontent.com/49863684/191887137-b14a364e-09f5-4f98-b9dc-c2484536a064.png">

We can apply our solution to "reversing a linked-list" in groups of k, whilst addressing the wiring in between each of the k-groups. As always, there is a recursive analog to our iterative solution, where we can begin by reversing the first k-nodes in our linked-list, then recursively calling our reverse function on the remainign nodes within our linked list. 

**First Missing Positive Integer:** Given an unsorted array of integers, return the smallest missing positive integer. 

<img width="710" alt="image" src="https://user-images.githubusercontent.com/49863684/191893369-b15ed114-9ee7-4f0d-8316-3a54e16fe0e1.png">

**Median of Two Sorted Arrays:** Given two worted arrays, output the median of both of the sorted arrays. 

**Longest Valid Parenthesis:** Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parantheses substring. 

**Wildcard Matching:** We will take a dynamic-programming approach. 

Some key takeaways:

1. Python dictionaries: We observe that python dictionaries are implemented as hash table, and allow for hash collisions i.e. even if two distinct keys have the same hash value, the table must still have a strategy to insert and retrieve the key and value pairs unambiguosly (the solution is to use "open addressing")

2. The python hash table is a contiguous block of memory, so we have an O(1) lookup time. Each slot in the table can store one and only one entry. Each entry in the table is a combination of <hash, key, value>. We take advantage of hash-tables to circumvent large time complexities that arise from iteration through unsorted/chaotic data. 

3. Python "self". Since python is an object-oriented programming language, every time we define methods for a class, we will use self as the very first parameter. The "self" parameter allows access to unique attributes and methods for each individual declaration of our object. 

4. Whenever we are provided with an O(log n) complexity bound, binary search is most likely involved in some capacity. 

**LRU Cache:** We would like to implement a caching mechanism that echibits the LRU eviction policy i.e. we will store a certain amount of data and evict the least recently used element when we call get() (there are two functions that our API must address, namely get() and put()). 

<img width="703" alt="image" src="https://user-images.githubusercontent.com/49863684/191903518-415b074e-b224-4547-9f64-58f5183d3fb6.png">

To keep track of ordering (i.e. how recently we have accessed a particular data element), we should utilize a structure such as a linked list, which allows us to dynamically change the ordering of our values as we go along. However, if we want to access elements efficiently as well, we should also use a data structure such as a hash-table, which will provide us with constant time access. Ultimately, we can combine the two data structures to provide us with both constant-time access and the ability to keep track of how recently we have accessed a particular element within our cache (image above). 

**Lowest Common Ancestor in BST:** We take a recursive approach. The key idea is that the lowest common ancestor A of nodes X and Y is the unique node satisfying the property that (WLOG) node X lies in it's left subtree child and node Y lies in it's right subtree child. 

**Serialize and Deserialize a Binary Tree:** This ADT should accomodate for two main functions ".serialize()" and ".deserialize()". We should apply the "single action, then defer" heuristic. Again, we should take a recursive approach on the left sub-tree and the right sub-trees, using the typical recursive structure for BST-type problems. 

**Find the k-th largest element in array:** A min-heap or a max-heap will readily allow us to find the k-th largest element in a particular set of leements, this should be the go-to approach. By maintaining a min-heap of size 2, once we burn through all of the elements in our array, since every time we evict the smallest element (root-node) of our min-heap, by the end of all of our iterations, we are left with only the two largest elements. 
