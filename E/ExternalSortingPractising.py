'''
-Easy-

描述
In this problem, you will get a series of files, there is a sorted array in every file, but you can 
not read them all at once.
So, in this problem, you need to implement a External Sorting Algorithm, to sort numbers in these files.
The parammeters in this problem include the following two:

files : it representing a series of files, and every file has an ascending array
result : it representing a file, and you need write your answer in this file
You will get a number in the i-th file by using files[i].read(), and after you get this number, this 
number will be deleted from this file.
For example: the sorted array in files[2] is [2,4,5], after using files[i].read(), the sorted 
array will become [4,5].

You can judge whether the i-th file is empty by using files[i].isEmpty(), if this function returns true, 
that means there is no data in the i-th file, if this function returns false, that means the i-th file is not empty.
For example: if there is no data in files[2], you will get true by using files[2].isEmpty().

You can write a number value into file result by using result.write(value).
For example: the array in result is [1,2,4], after using result.write(10), the array in result will become [1,2,4,10].

The function in this problem does not need any return value, the evaluation system will determine if your 
code is correct by checking the file result.

样例
Example 1:

Input:

files = [[1,3,5],[2,5],[4,7]]
Output:

[1,2,3,4,5,5,7]
查看提示

'''

import heapq

class Solution:
    """
    @param files: some files with integers need to be sorted
    @param result: a file for writing numbers
    @param n: numbers of files
    @return: nothing
    """

    def sortOnDisk(self, files, result):
        # write your code here
        pq = []
        for i,f in enumerate(files):
            heapq.heappush(pq, (f.read(), i))
        #print(dir(files[0]))
        while pq:
            cur, idx = heapq.heappop(pq)
            result.write(cur)
            if not files[idx].is_empty():
                heapq.heappush(pq, (files[idx].read(), idx))