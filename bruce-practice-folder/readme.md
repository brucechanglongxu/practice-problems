Maximum Contiguous Subarray:
The most efficient solution is a direct sorting algorithm, followed by a two-pointer gradual increment. This reduces a-lot of the unnecessary work that is done when we naively iterate over all of the possible contiguous subarrays and find their sum. 

Two Sum: 
A dynamic programming solution allows to reduce the solution time complexity from O(N^2) to O(N)

Some key takeaways:

1. Python dictionaries: We observe that python dictionaries are implemented as hash table, and allow for hash collisions i.e. even if two distinct keys have the same hash value, the table must still have a strategy to insert and retrive the key and value pairs unambiguosly (the solution is to use "open addressing")

2. The python hash table is a contiguous block of memory, so we have an O(1) lookup time. Each slot in the table can store one and only one entry. 

3. Each entry in the table is a combination of <hash, key, value>


