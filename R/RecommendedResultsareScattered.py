'''

-Easy-

A recommendation system will recommend a list of video and picture elements. x is the element number, 
V_x is the video, and P_x is the image.Now you need to shatter these elements, and the rules are as follows:

The position of the first [picture P] remains unchanged;
Starting from the first [picture P], there is exactly 1 [picture P] in every n element;
The relative order between the pictures remains unchanged;
Elements that do not satisfy the shatter rule need to be discarded. Give you the list of elements 
and the value of n, please return the list of elements after scattering.

1 ≤ number of elements ≤10000
2 ≤ n ≤ number of elements
Make sure there's at least 1 [picture P] in the elements.

样例
Example 1:
Input sample:
elements=["V_0", "V_1", "V_2", "P_3", "P_4", "P_5", "V_6", "P_7", "V_8", "V_9"] , n=3
Output sample:
["V_0", "V_1", "V_2", "P_3", "V_6", "V_8", "P_4", "V_9"]
Sample explanation:
P_3 needs to appear in the 3rd bit starting from 0, since there is exactly 1 P in every 3 elements. P_5 and P_7 cannot meet the shatter requirements, so they are deleted.

Example 2:
Input sample:
elements=["V_0", "P_1", "V_2", "V_3", "V_4"] , n=2
Output sample:
["V_0", "P_1", "V_2"]
Sample explanation:
P_1 needs to appear in the first bit starting from 0, since there is exactly 1 P in every 2 elements. V_3 and V_4 cannot meet the shatter requirements, so they are deleted.

标签

'''

class Solution:
    """
    @param elements: A list of recommended elements.
    @param n: [picture P] can appear at most 1 in every n
    @return: Return the scattered result.
    """
    def scatter(self, elements, n):
        # write your code here
        res = []
        i = 0
        while i < len(elements):
            e = elements[i] 
            if e[0] == 'P': break
            res.append(e)
            i += 1
        P, V = [], []        
        for j in range(i, len(elements)):
            e = elements[j] 
            if e[0] == 'P': P.append(e)
            else: V.append(e)
        i, j, k = 0, 0, n-1
        while i < len(P) and j < len(V):
            if i < len(P):
                res.append(P[i])
                i += 1
            k = 0
            while j < len(V) and k < n-1:
                res.append(V[j])
                j += 1
                k += 1 
        if k == n-1 and i < len(P):
            res.append(P[i]) 
        return res



if __name__=="__main__":
    #print(Solution().scatter(elements=["V_0", "V_1", "V_2", "P_3", "P_4", "P_5", "V_6", "P_7", "V_8", "V_9"] , n=3))
    #print(Solution().scatter(elements=["V_0", "P_1", "V_2", "V_3", "V_4"] , n=2))
    #print(Solution().scatter(["V_0", "P_1", "V_2", "V_3", "P_4", "V_5", "V_6", "P_7", "P_8", "P_9"],2))
    #print(Solution().scatter(["V_0","V_1","V_2","P_3","P_4","P_5","V_6","P_7","V_8","V_9"], 3))
    print(Solution().scatter(["V_0", "V_1", "V_2", "V_3", "V_4", "V_5", "V_6", "V_7", "V_8", "P_9"], 2))