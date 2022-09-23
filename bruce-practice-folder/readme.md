**Reverse Linked List:** 
The iterative solution utilizes multiple O(1) rewriting moves, and since we pass through the entire array, we require O(n) time and constant space overhead (since we only need to maintain three pointers, curr, prev and next at all times throughout our entire algorithm). 

<img width="728" alt="image" src="https://user-images.githubusercontent.com/49863684/191891691-dc2c2c18-b4c3-494b-a51f-f430e2c4c410.png">

The recursive solution is easier to reason about, but requires more computational/space overhead O(n) compared to the iterative solution (since we need to create n stack frames throughout our recursion), we can re-wire the first node of our linked list, and subsequently recursively call our Reverse() function on the remainder of the linked list. 

**Reverse Node in k-group:** Given a linked list, reverse the elements in the linked list in groups of k at a time. 

<img width="740" alt="image" src="https://user-images.githubusercontent.com/49863684/191887137-b14a364e-09f5-4f98-b9dc-c2484536a064.png">

We can apply our solution to "reversing a linked-list" in groups of k, whilst addressing the wiring in between each of the k-groups. As always, there is a recursive analog to our iterative solution, where we can begin by reversing the first k-nodes in our linked-list, then recursively calling our reverse function on the remainign nodes within our linked list. 

**First Missing Positive Integer:** Given an unsorted array of integers, return the smallest missing positive integer. 

<img width="710" alt="image" src="https://user-images.githubusercontent.com/49863684/191893369-b15ed114-9ee7-4f0d-8316-3a54e16fe0e1.png">

Some key takeaways:

1. Python dictionaries: We observe that python dictionaries are implemented as hash table, and allow for hash collisions i.e. even if two distinct keys have the same hash value, the table must still have a strategy to insert and retrieve the key and value pairs unambiguosly (the solution is to use "open addressing")

2. The python hash table is a contiguous block of memory, so we have an O(1) lookup time. Each slot in the table can store one and only one entry. Each entry in the table is a combination of <hash, key, value>. We take advantage of hash-tables to circumvent large time complexities that arise from iteration through unsorted/chaotic data. 

4. Python "self". Since python is an object-oriented programming language, every time we define methods for a class, we will use self as the very first parameter. The "self" parameter allows access to unique attributes and methods for each individual declaration of our object. 


