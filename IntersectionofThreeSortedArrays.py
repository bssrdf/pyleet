'''
-Easy-

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, 
return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
Hints
Count the frequency of all elements in the three arrays.
The elements that appeared in all the arrays would have a frequency of 3.

'''

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        # You may notice that Approach 1 does not utilize the fact that all arrays are sorted . Indeed, 
        # instead of using a Hashmap to store the frequencies, we can use three pointers p1 , p2 , 
        # and p3 to iterate through arr1 , arr2 , and arr3 accordingly:

        #Each time, we want to increment the pointer that points to the smallest number, i.e., 
        # min(arr1[p1], arr2[p2], arr3[p3]) forward;
        #if the numbers pointed to by p1 , p2 , and p3 are the same, we should then store it and 
        # move all three pointers forward.
        #Moreover, we don't have to move the pointer pointing to the smallest number - we only 
        # need to move the pointer pointing to a smaller number. In this case, we avoid comparing 
        # three numbers and finding the smallest one before deciding which one to move. You may 
        # find the rationale behind this in the Algorithm.

        #!?!../Documents/1213_Intersection_of_Three_Sorted_Arrays.json:531,198!?!

        #Algorithm

        #Initiate three pointers p1 , p2 , p3 , and place them at the beginning of arr1 , arr2 , arr3 by initializing them to 0;
        #while they are within the boundaries:
        #if arr1[p1] == arr2[p2] && arr2[p2] == arr3[p3] , we should store it because it appears three times in arr1 , arr2 , and arr3 ;
        #else
        #if arr1[p1] < arr2[p2] , move the smaller one, i.e., p1 ;
        #else if arr2[p2] < arr3[p3] , move the smaller one, i.e., p2 ;
        #if neither of the above conditions is met, it means arr1[p1] >= arr2[p2] && arr2[p2] >= arr3[p3] , therefore move p3 .

        ans = []
        # prepare three pointers to iterate through three arrays
        # p1, p2, and p3 point to the beginning of arr1, arr2, and arr3 accordingly
        p1 = p2 = p3 = 0
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                ans.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1
        return ans

if __name__ == "__main__":
    print(Solution().arraysIntersection(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]))
