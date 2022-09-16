# Leetcode Patterns

## Some common patterns distilled from hard problems. They are categorised as:

- Sliding Window

  - Given some items or tasks, you have to take or complete in the given order with some  constraints (weight, time...). This is a typical sliding window pattern: maintain a window [left, right], iterate over the items/tasks, and keep accumulating the needed quantity, once that quantity violates the constraint, shrink the window by moving left forward; in this process, compute what is asked for, e.g. min/max length etc. See 
  
    - [1687. Delivering Boxes from Storage to Ports](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/)

    Sometimes, one needs more advanced data structure to find certain quantities, e.g. **monotonic queue** can be used to find the max/min within the window; the monotonic queue can maintain max/min while the window is shrinking. See
    - [2398. Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/)



- Segment Tree

  - Given some items or tasks in an array, you go through them one by one following the given order. When at *i*-th item, you need to find a max/min/sum over a certain range [x, y]. Segment tree is especially useful in this **point update, range query** case. Initialize a segment tree; within the i-loop, query the range and get the results and then do an update using the information obtained so far. See 

    - [2407. Longest Increasing Subsequence II](https://leetcode.com/problems/longest-increasing-subsequence-ii/)    

  




