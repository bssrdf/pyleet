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

&nbsp;<br>
- Subarray Bitwise Product
  
  - Given an integer array, you need to find the min/max length of a subarray where the OR/AND/XOR product satisfies certain requirement. The pattern is to consider each bit of integer individually and then combine all bits together to find answer. See

    - [2411. Smallest Subarrays With Maximum Bitwise OR](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) 
  
&nbsp;<br>
- Construct graph following a certain order of edges 

  - Given a series of undirected edges, the problem is to find number of paths satisfying certain requirements. The underlying idea is **MST** using **Union Find**. Build the graph one edge a step; compute certain properties using the current connectivity information; union the two nodes and move on to next edge. See

    - [2421. Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/) 
    - [1697. Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)
    - [1724. Checking Existence of Edge Length Limited Paths II](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/)




  




