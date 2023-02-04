'''
-Hard-

In a project, you have a list of required skills req_skills, and a list of people. The ith 
person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, 
there is at least one person in the team who has that skill. We can represent these teams by 
the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. 
You may return the answer in any order.

It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] consists of lowercase English letters.
All the strings of req_skills are unique.
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] consists of lowercase English letters.
All the strings of people[i] are unique.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.

'''
from functools import lru_cache
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        n = len(req_skills)
        m = len(people)
        sid = {s:i for i,s in enumerate(req_skills)}
        @lru_cache(None)
        def dp(start, mask):
            if mask == 0: return [0,[]] # base case, about to start the 1st session
            #if start == m: return [] 
            ans = [m, []]
            st = set()
            for j in range(start, m):
                nmask = 0
                for ski in people[j]:                    
                   if mask & (1<<sid[ski]): 
                       nmask += 1<<sid[ski]
                if nmask in st: continue
                st.add(nmask)    
                nm, candidates = dp(j+1, mask-nmask) # find the total # of sessions and time over the 
                                                       # last accumulated without taking j-th task
                if ans[0] > nm:                                       
                    ans[0] = nm+1
                    ans[1] = [j]+candidates
            return ans

        return dp(0, (1<<n) - 1)[1]
        

if __name__ == "__main__":
    req_skills = ["java","nodejs","reactjs"]; people = [["java"],["nodejs"],["nodejs","reactjs"]]
    print(Solution().smallestSufficientTeam(req_skills, people))
    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    print(Solution().smallestSufficientTeam(req_skills, people))
    