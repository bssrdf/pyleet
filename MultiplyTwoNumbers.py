'''

-Easy-

Given two numbers represented by linked lists, write a function that returns the multiplication 
of these two linked lists.

样例
Example 1:

Input：9->4->6->null,8->4->null
Output：79464
Explanation：946*84=79464
Example 2:

Input：3->2->1->null,1->2->null
Output：3852
Explanation：321*12=3852


'''

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the product list of l1 and l2
    """
    def multiplyLists(self, l1, l2):
        # write your code here
        cur1, cur2 = l1, l2
        ans, num1 = 0, 0
        while cur1:
            num1 = 10*num1+cur1.val        
            cur1 = cur1.next
        cur2 = l2
        while cur2:
            ans += 10*ans+cur2.val*num1
            cur2 = cur2.next
        return ans
