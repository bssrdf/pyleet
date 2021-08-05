'''
-Medium-
*Greedy*
You are given a series of video clips from a sporting event that lasted time seconds. 
These video clips can be overlapping with each other and have varying lengths.

Each video clip is described by an array clips where clips[i] = [starti, endi] indicates 
that the ith clip started at starti and ended at endi.

We can cut these clips into segments freely.

For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that 
cover the entire sporting event [0, time]. If the task is impossible, return -1.

 

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:

Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation: We can't cover [0,5] with only [0,1] and [1,2].
Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
Output: 3
Explanation: We can take clips [0,4], [4,7], and [6,9].
Example 4:

Input: clips = [[0,4],[2,8]], time = 5
Output: 2
Explanation: Notice you can have extra video after the event ends.
 

Constraints:

1 <= clips.length <= 100
0 <= starti <= endi <= 100
1 <= time <= 100

'''

class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        rangeMap = [0]*(time+1) # 用于存储每个起点能覆盖到的最大范围
        for clip in clips: 
            if clip[0] > time: continue
            rangeMap[clip[0]] = max(rangeMap[clip[0]], clip[1])
        # 从0开始，看其最远覆盖范围是多少。
        currendEnd = rangeMap[0]
        # 返回结果，将0计入次数中，所以初始值为1
        res = 1
        # 因为0已经预先定义好，所以从1开始循环
        i = 1
        # 当currendEnd 大于等于目标值T时，结束循环
        while currendEnd < time:
            # 定义下一个最远覆盖范围
            nextMaxEnd = 0
            # 从当前位置到currendEnd范围内的所有数为起点，找其能覆盖的最远距离
            for j in range(i, currendEnd+1):
                nextMaxEnd = max(nextMaxEnd, rangeMap[j])
            # 如果找到的最远距离无法超越currendEnd，说明后续片段无法连接
            if nextMaxEnd <= currendEnd:
                return -1
            # 将i至于currendEnd之后
            i = currendEnd + 1
            # 当前能覆盖的最远距离更新为nextMaxEnd
            currendEnd = nextMaxEnd
            # 次数加一
            res += 1
        return res

if __name__ == "__main__":
    print(Solution().videoStitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10))
    print(Solution().videoStitching(clips = [[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10))