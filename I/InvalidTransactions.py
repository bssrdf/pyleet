'''
-Medium-

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same 
name in a different city.
Each transaction string transactions[i] consists of comma separated values 
representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  
You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs 
within a difference of 60 minutes, have the same name and is in a different city. 
Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths 
between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.

'''

from collections import namedtuple

class Solution(object):

    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        Trans = namedtuple('Trans', 'name time amount city')
        tarr = []
        res = []
        for trans in transactions:
            args = trans.split(',')
            tarr.append(Trans(*args))
        n = len(tarr)
        for i in range(n):
            if int(tarr[i].amount) > 1000:
                res.append(','.join(list(tarr[i])))
                continue
            found = False
            for j in range(n):
                if i == j: continue
                if tarr[i].name == tarr[j].name  and  \
                   tarr[i].city != tarr[j].city  and \
                     abs(int(tarr[i].time)-int(tarr[j].time)) <= 60:
                    found = True
                    break
            if found:
                res.append(','.join(list(tarr[i])))
                found = False
        return res                   
        
if __name__ == "__main__":
    #print(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
    #trans = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona",
    #"bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]

    #trans = ["bob,627,1973,amsterdam","alex,387,885,bangkok","alex,355,1029,barcelona",
    #        "alex,587,402,bangkok","chalicefy,973,830,barcelona","alex,932,86,bangkok",
    #        "bob,188,989,amsterdam"]
    trans = ["chalicefy,639,1283,beijing","maybe,324,192,frankfurt","bob,627,974,amsterdam",
    "alex,962,125,chicago","iris,849,36,beijing","chalicefy,70,415,bangkok",
    "chalicefy,112,467,frankfurt","xnova,358,82,barcelona","chalicefy,180,543,beijing",
    "xnova,624,572,budapest","lee,651,1761,chicago","alex,991,1698,budapest",
    "bob,531,700,amsterdam","chalicefy,926,478,budapest","iris,235,1993,frankfurt",
    "alex,107,812,beijing","maybe,199,1313,barcelona"]
    #print(Solution().invalidTransactions(trans))
    #print(Solution().invalidTransactionsNLogN(trans))
    trans = ["bob,649,842,prague","alex,175,1127,mexico","iris,164,119,paris","lee,991,1570,mexico","lee,895,1876,taipei","iris,716,754,moscow","chalicefy,19,592,singapore","chalicefy,820,71,newdelhi","maybe,231,1790,paris","lee,158,987,mexico","chalicefy,415,22,montreal","iris,803,691,milan","xnova,786,804,guangzhou","lee,734,1915,prague","bob,836,1904,dubai","iris,666,231,chicago","iris,677,1451,milan","maybe,860,517,toronto","iris,344,1452,bangkok","lee,664,463,frankfurt","chalicefy,95,1222,montreal","lee,293,1102,istanbul","maybe,874,36,hongkong","maybe,457,1802,montreal","xnova,535,270,munich","iris,39,264,istanbul","chalicefy,548,363,barcelona","lee,373,184,munich","xnova,405,957,mexico","chalicefy,517,266,luxembourg","iris,25,657,singapore","bob,688,451,beijing","bob,263,1258,tokyo","maybe,140,222,amsterdam","xnova,852,330,barcelona","xnova,589,837,budapest","lee,152,981,mexico","alex,893,1976,shenzhen","xnova,560,825,prague","chalicefy,283,399,zurich","iris,967,1119,guangzhou","alex,924,223,milan","chalicefy,212,1865,chicago","alex,443,537,taipei","maybe,390,5,shanghai","bob,510,1923,madrid","bob,798,343,hongkong","iris,643,1703,madrid","bob,478,928,barcelona","maybe,75,1980,shanghai","xnova,293,24,newdelhi","iris,176,268,milan","alex,783,81,moscow","maybe,560,587,milan","alex,406,776,istanbul","lee,558,727,paris","maybe,481,1504,munich","maybe,685,602,madrid","iris,678,788,madrid","xnova,704,274,newdelhi","chalicefy,36,1984,paris","iris,749,200,amsterdam","lee,21,119,taipei","iris,406,433,bangkok","bob,777,542,taipei","maybe,230,1434,barcelona","iris,420,1818,zurich","lee,622,194,amsterdam","maybe,545,608,shanghai","xnova,201,1375,madrid","lee,432,520,dubai","bob,150,1634,singapore","maybe,467,1178,munich","iris,45,904,beijing","maybe,607,1953,tokyo","bob,901,815,tokyo","maybe,636,558,milan","bob,568,1674,toronto","iris,825,484,madrid","iris,951,930,dubai","bob,465,1080,taipei","bob,337,593,chicago","chalicefy,16,176,rome","chalicefy,671,583,singapore","iris,268,391,chicago","xnova,836,153,jakarta","bob,436,530,warsaw","alex,354,1328,luxembourg","iris,928,1565,paris","xnova,627,834,budapest","xnova,640,513,jakarta","alex,119,16,toronto","xnova,443,1687,taipei","chalicefy,867,1520,montreal","alex,456,889,newdelhi","lee,166,3,madrid","bob,65,1559,zurich","alex,628,861,moscow","maybe,668,572,mexico","bob,402,922,montreal"]
    #print(Solution().invalidTransactions(trans))
    sol1 = Solution().invalidTransactions(trans)
    