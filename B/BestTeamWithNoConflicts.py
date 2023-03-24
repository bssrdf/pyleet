'''
-Medium-
*DP*
*Sorting*
*Fenwick Tree*

You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
Example 2:

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
Example 3:

Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
 

Constraints:

1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 106
1 <= ages[i] <= 1000

'''


from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = [[a, s] for a, s in zip(ages, scores)]
        players.sort(reverse = True)
        
        ans = 0
        dp = [0]*n
        
        for i in range(n):
            score = players[i][1]
            dp[i] = score
            for j in range(i):
                if players[j][1] >= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])
        
        return ans

    def bestTeamScore2(self, scores: List[int], ages: List[int]) -> int:
        # the idea is similar to finding the LIS
        # only here to find longest non-decending sequence of score
        # after sorting them based on age
        # all players from the sequence can form a valid team
        n = len(scores)
        players = [[a, s] for a, s in zip(ages, scores)]
        players.sort()
        
        ans = 0
        dp = [0]*n
        
        for i in range(n):
            score = players[i][1]
            dp[i] = score
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])        
        return ans    
    
    def bestTeamScore3(self, scores: List[int], ages: List[int]) -> int:
        '''
        In the binary indexed tree, we store some information which will be the 
        score in our case, corresponding to indices which will be the age here. 
        Hence, a node in the binary indexed tree with index x will store the 
        maximum score possible with players with age <= x.

        We will sort the players in ascending order of their score and then by age. 
        Then we will iterate over each player, and for each player with age x, we 
        will find the maximum score with players having age less than or equal to x 
        by querying the BIT. This maximum score can be added to the current player 
        score as we have sorted the players, so the current score will be the 
        maximum seen so far and won't cause a conflict.

        Now that the maximum score with age x is the above addition currentBest 
        (current player score and the BIT returned query result), we need to 
        update the BIT so that all the nodes with age greater than x have the 
        updated values. The maximum of all the currentBest is the maximum 
        score we can get.

        This approach is similar to the previous two where we iterate over 
        the players and for each player, find the maximum non-conflicting score. 
        In the previous two approaches, we needed linear time to find the 
        non-conflicting score, but with a BIT we only need logarithmic time.

        Algorithm

        Store the ages and scores of all the players in the list ageScorePair.

        Sort the list ageScorePair in ascending order of score and then in 
        ascending order of age.

        Find the maximum age in the list and store it as highestAge. Create an 
        array BIT with size highestAge + 1; this is the binary indexed tree.

        Iterate over players from 0 to N - 1 for each player pair ageScore:

        Store the maximum score possible with this player as the currentBest. 
        This will be equal to the sum of the current player score and the score 
        returned by querying BIT with a score up to this age.

        Update the score in BIT with an age greater than the current player age 
        if their score is smaller than currentBest.

        Store the maximum of all currentBest in the variable answer.

        Return answer.
        '''
        n = len(scores)
        ageScorePair = [(s, a) for a, s in zip(ages, scores)]
        ageScorePair.sort()
        ans, highestAge = 0, max(ages)
        bit = [0]*(highestAge+1)
        def update(i, x):
            while i <= highestAge:
                bit[i] = max(bit[i], x)
                i += i & (-i)
        def query(i):
            t = 0
            while i > 0:
                t = max(t, bit[i])
                i -= i & (-i)
            return t
        for i in range(n):
            score = ageScorePair[i][0]
            age = ageScorePair[i][1]
            currentBest = score + query(age)
            ans = max(ans, currentBest)
            update(age, currentBest)
        return ans    


if __name__ == "__main__":
    print(Solution().bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))  
    print(Solution().bestTeamScore3(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))     