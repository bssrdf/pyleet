# Leetcode Patterns

## Some common patterns distilled from hard problems. They are categorised as:

- Sliding Window

  - Given some items or tasks, you have to take or complete in the given order with some  constraints (weight, time...). This is a typical sliding window pattern: maintain a window [left, right], iterate over the items/tasks, and keep accumulating the needed quantity, once that quantity violates the constraint, shrink the window by moving left forward; in this process, compute what is asked for, e.g. min/max length etc. See 
  
    - [1687. Delivering Boxes from Storage to Ports](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/)
    &nbsp;<br>
    If the needed quantity is sum over subarrays and constraint is the sum <= K, and the goal is to find the number of subarrays that satisfy the constraint, the pattern looks something like:
      ```python
       l, r = 0, 0  
       nSubs = 0 # number of subarray satsifying the constraint 
       while r < n:
           sums += nums[r]
           r += 1
           while sums > k:
              sums -= nums[l]
              l += 1
          nSubs += r-l
       return nSubs  
       ```  
      see   
    - [Kth Smallest Subarray Sum](https://github.com/doocs/leetcode/blob/main/solution/1900-1999/1918.Kth%20Smallest%20Subarray%20Sum/README_EN.md)   
    &nbsp;<br>
    Sometimes, one needs more advanced data structure to find certain quantities, e.g. **monotonic queue** can be used to find the max/min within the window; the monotonic queue can maintain max/min while the window is shrinking. See
    - [2398. Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/)


&nbsp;<br>
- Segment Tree

  - Given some items or tasks in an array, you go through them one by one following the given order. When at *i*-th item, you need to find a max/min/sum over a certain range [x, y]. Segment tree is especially useful in this **point update, range query** case. Initialize a segment tree; within the i-loop, query the range and get the results and then do an update using the information obtained so far. See 

    - [2407. Longest Increasing Subsequence II](https://leetcode.com/problems/longest-increasing-subsequence-ii/)   

- Fenwick Tree
  
  - Similar idea to above segment tree. Given some items or tasks in an array, you go through them one by one following the given order. When at *i*-th item, you need to find a max/min/sum over a certain range [x, y], typically [0, y]. Fenwick tree is especially useful in this **point update, range query** case. Initialize a Fenwick tree; within the i-loop, query the range and get the results and then do an update using the information obtained so far. See 
    - [2926. Maximum Balanced Subsequence Sum](https://leetcode.com/problems/maximum-balanced-subsequence-sum/) 
        

&nbsp;<br>
- Subarray Bitwise Product
  
  - Given an integer array, you need to find the min/max length of a subarray where the OR/AND/XOR product satisfies certain requirement. The pattern is to consider each bit of integer individually and then combine all bits together to find answer. See

    - [2411. Smallest Subarrays With Maximum Bitwise OR](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) 
  

  - Given an integer array, you need to find the number of subarrays on which the bitwise product satisfies certain conditions, e.g. the XOR product is zero. This kind of problems are often tied to the idea of prefix sum: the product over ```A[:i]``` (call it ```S_0_i```) is equal to product of ```S_0_j``` and ```S_j_i```. Then such problems can be transformed to find the number of subarrays which have ```S_j_i = y```. Let the product be XOR product, ```S_0_i = x1^x2....^xi``` and ```S_j_i = xj^...^xi = S_0_i^S_0_j```. We can use a map to store the frequency of ```S_0_j``` and at each ```i``` query the map to get the number of ```S_0_i```, i.e., the number of subarrays that can be formed by ```j``` and ```i```. See
    - [2588. Count the Number of Beautiful Subarrays](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/)   
  
&nbsp;<br>
- Construct graph following a certain order of edges 

  - Given a series of undirected edges, the problem is to find number of paths satisfying certain requirements. The underlying idea is **MST** using **Union Find**. Build the graph one edge a step; compute certain properties using the current connectivity information; union the two nodes and move on to next edge. See

    - [2421. Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/) 
    - [1697. Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)
    - [1724. Checking Existence of Edge Length Limited Paths II](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/)

&nbsp;<br>
- DFS that can be memoized
  - Certain graph/tree problems which require DFS solutions can also use memoization to speed
  up the process. This could make a seemingly O(N^2) solution to pass AC. The dfs function looks
  like 
  ```python
  @lru_cache(None)
  def dfs(node, parent):
      ret = 0
      for child in G[node]:
        if child == parent: continue
        # some operations on ret 
        ret += dfs(child, parent) # accumulate results from child nodes 
      return ret   
  for i in range(n):    
     dfs(i, -1) # call dfs for each node
                # this is O(n^2) but memoization will make it much faster in practice                
  ```  
  See [2581. Count Number of Possible Root Nodes](https://leetcode.com/problems/count-number-of-possible-root-nodes/description/) and [2538. Difference Between Maximum and Minimum Price Sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/)

&nbsp;<br>
- Divide array elements into groups based on modular operation

  - Some problems can be solved by first divide the array elements into groups based on 
    $arr[i]\%k$ where $k$ is a parameter. Within each group, all the elements have the same 
    $\%k$ value; or they are multiples of $k$ ($0*k, 1*k, 2*k, ....$) apart. See [2638. Count the Number of K-Free Subsets](https://github.com/doocs/leetcode/blob/main/solution/2600-2699/2638.Count%20the%20Number%20of%20K-Free%20Subsets/README.md) 






  




