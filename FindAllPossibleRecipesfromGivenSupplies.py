'''

-Medium-

You have information about n different recipes. You are given a string array recipes 
and a 2D string array ingredients. The ith recipe has the name recipes[i], and you 
can create it if you have all the needed ingredients from ingredients[i]. Ingredients 
to a recipe may need to be created from other recipes, i.e., ingredients[i] may 
contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you 
initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.



'''

from typing import List
from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        nodes = recipes + supplies
        idx = {v:i for i,v in enumerate(nodes)}
        n = len(nodes)
        indeg = [0]*n
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[idx[ing]].append(i)
                indeg[i] += 1                
        que = deque()                   
        for i in range(n):
            if indeg[i] == 0:
                que.append(i)  
        # print(indeg, que)
        while que:
            u = que.popleft()
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    que.append(v)
        # print(indeg)
        return [recipes[i] for i in range(len(recipes)) if indeg[i] == 0]
    
    def findAllRecipes2(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = {v:0 for v in recipes+supplies}
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                indeg[recipes[i]] += 1                
        que = deque()                   
        for i in indeg:
            if indeg[i] == 0:
                que.append(i)  
        while que:
            u = que.popleft()
            for v in graph[u]:
                if v in indeg:
                    indeg[v] -= 1
                    if indeg[v] == 0:                       
                        indeg.pop(v)
                        que.append(v)
        return [r for r in recipes if r not in indeg] 




if __name__ == "__main__":
    recipes = ["bread"]; ingredients = [["yeast","flour"]]; supplies = ["yeast","flour","corn"]
    print(Solution().findAllRecipes(recipes, ingredients, supplies))   
    print(Solution().findAllRecipes2(recipes, ingredients, supplies))   
    recipes = ["bread","sandwich"] 
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"] 
    print(Solution().findAllRecipes(recipes, ingredients, supplies))   
    print(Solution().findAllRecipes2(recipes, ingredients, supplies))   
    recipes = ["bread","sandwich","burger"] 
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    print(Solution().findAllRecipes(recipes, ingredients, supplies))   
    print(Solution().findAllRecipes2(recipes, ingredients, supplies))   
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast"]
    # print(Solution().findAllRecipes(recipes, ingredients, supplies))   
    print(Solution().findAllRecipes2(recipes, ingredients, supplies))   
