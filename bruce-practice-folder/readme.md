**Maximum Contiguous Subarray:**
The most efficient solution is a direct sorting algorithm, followed by a two-pointer gradual increment. This reduces a-lot of the unnecessary work that is done when we naively iterate over all of the possible contiguous subarrays and find their sum. 

**Two Sum:** 
A dynamic programming solution allows to reduce the solution time complexity from O(N^2) to O(N)

**Reverse Linked List:** 
The iterative solution utilizes multiple O(1) rewriting moves, and since we pass through the entire array, we require O(n) time and constant space overhead. 

<img width="651" alt="image" src="https://user-images.githubusercontent.com/49863684/191865895-77934d0a-9876-4563-b570-a4cf173e84d1.png">

The recursive solution is easier to reason about, but requires more computational/space overhead (O(n)) compared to the iterative solution, there are various sections of the linked list that we can actually call our recursive function on. 

**Same Tree:**
Our solution is recursive in nature. 

**Reverse Node in k-group:** Given a linked list, reverse the elements in the linked list in groups of k at a time. 

<img width="740" alt="image" src="https://user-images.githubusercontent.com/49863684/191887137-b14a364e-09f5-4f98-b9dc-c2484536a064.png">

We can apply our solution to "reversing a linked-list" in groups of k, whilst addressing the wiring in between each of the k-groups. As always, there is a recursive analog to our iterative solution, where we can begin by reversing the first k-nodes in our linked-list, then recursively calling our reverse function on the remainign nodes within our linked list. 

Some key takeaways:

1. Python dictionaries: We observe that python dictionaries are implemented as hash table, and allow for hash collisions i.e. even if two distinct keys have the same hash value, the table must still have a strategy to insert and retrive the key and value pairs unambiguosly (the solution is to use "open addressing")

2. The python hash table is a contiguous block of memory, so we have an O(1) lookup time. Each slot in the table can store one and only one entry. 

3. Each entry in the table is a combination of <hash, key, value>

4. Python "self". Since python is an object-oriented programming language, every time we define methods for a class, we will use self as the very first parameter. The "self" parameter allows access to unique attributes and methods for each individual declaration of our object. 


