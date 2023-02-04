'''

-Medium-

In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the 
competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the 
first position, we consider the second position to resolve the conflict, if they tie again, we continue this 
process until the ties are resolved. If two or more teams are still tied after considering all positions, 
we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams 
according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

 

Example 1:

Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.
Example 2:

Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 
Example 3:

Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter so his votes are used for the ranking.
Example 4:

Input: votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
Output: "ABC"
Explanation: 
Team A was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team B was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team C was ranked first by 2 voters, second by 2 voters and third by 2 voters.
There is a tie and we rank teams ascending by their IDs.
Example 5:

Input: votes = ["M","M","M","M"]
Output: "M"
Explanation: Only team M in the competition so it has the first rank.
 

Constraints:

1 <= votes.length <= 1000
1 <= votes[i].length <= 26
votes[i].length == votes[j].length for 0 <= i, j < votes.length.
votes[i][j] is an English upper-case letter.
All characters of votes[i] are unique.
All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.

'''

from typing import List
from collections import defaultdict
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes)
        m = len(votes[0])
        print('n, m', n,m)
        books = [defaultdict(int) for _ in range(26)]
        score = [0]*26
        for s in votes:
            for i,c in enumerate(s):
                if c == 'R':
                    print(i)
                score[ord(c)-ord('A')] += (m-i)
                books[ord(c)-ord('A')][i] += 1
        #print(score)
        #print([chr(i+ord('A')) for i,s in enumerate(score)])
        print([(k, books[ord('R')-ord('A')][k]) for k in sorted(books[ord('R')-ord('A')].keys())])
        print([(k, books[ord('V')-ord('A')][k]) for k in sorted(books[ord('V')-ord('A')].keys())])
        ranks = [(s,i) for i,s in enumerate(score)]
        ranks.sort(key=lambda x: (-x[0],x[1]))
        res = ''
        for s,i in ranks: 
            if s != 0:
                res += chr(i+ord('A'))
        return res

    def rankTeams2(self, votes: List[str]) -> str:
        n = len(votes)
        m = len(votes[0])
        ranks = [[0]*m for _ in range(26)]
        for s in votes:
            for i,c in enumerate(s):
                ranks[ord(c)-ord('A')][i] += 1
        teams = [i for i in range(26)]
        teams.sort(key=lambda x: tuple(-ranks[x][y] for y in range(m))+(x,))    

        return ''.join([chr(t+ord('A')) for t in teams if chr(t+ord('A')) in votes[0]])

    

        
if __name__ == "__main__":
    print(Solution().rankTeams2(["ABC","ACB","ABC","ACB","ACB"]))
    print(Solution().rankTeams2(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
    print(Solution().rankTeams2(["M","M","M","M"]))
    print(Solution().rankTeams2(["BCA","CAB","CBA","ABC","ACB","BAC"]))
    print(Solution().rankTeams2(["WXYZ","XYZW"]))
    votes = ["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]
    #print(Solution().rankTeams(votes))
    print(Solution().rankTeams2(votes))

