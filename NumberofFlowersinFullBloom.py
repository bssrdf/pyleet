'''

-Hard-

You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] 
means the ith flower will be in full bloom from starti to endi (inclusive). You are 
also given a 0-indexed integer array persons of size n, where persons[i] is the time 
that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers 
that are in full bloom when the ith person arrives.

 

Example 1:


Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:


Input: flowers = [[1,10],[3,3]], persons = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
 

Constraints:

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= persons.length <= 5 * 104
1 <= persons[i] <= 109



'''

from tracemalloc import start
from typing import List

from collections import defaultdict

class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0] * (n + 1)
        self.n = n
 
    def lowbit(self, x):
        return x & -x
 
    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
    
    def update(self, x, val):
        self.add(x, val)

    def range_update(self, ui, uj, val):
        self.update(ui, val)
        self.update(uj+1, -val)
 
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res

    def point_query(self, x):
        return self.sum(x)

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        #TLE
        events = []
        start, end = defaultdict(int), defaultdict(int)
        for s, e in flowers:
            start[s] += 1
            end[e] += 1 
        for s in start:
            events.append((s, -1, start[s]))
        for e in end:
            events.append((e, 1, end[e]))       
        p2i = defaultdict(list)
        for i,v in enumerate(persons):
            p2i[v].append(i)
        for t in p2i:
            events.append((t, 0, len(p2i[t])))
        events.sort() 

        ans = [0]*len(persons)
        cnt = 0
        for x, t, c in events:
            if t == -1:
                cnt += c
            elif t == 1:
                cnt -= c
            else:
                for j in p2i[x]:
                    ans[j] = cnt
        return ans
        

    def fullBloomFlowers2(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        cords = set() #defaultdict(int)
        for x,y in flowers:
            cords.add(x) 
            cords.add(y)              
        for p in persons:
            cords.add(p)
        n = len(cords)
        m = {}
        for i, x in enumerate(sorted(cords), start=1):
            m[x] = i      
        bit =  FenwickTree(n)
        for s,e in flowers:
            bit.range_update(m[s], m[e], 1)
        ans = []
        for p in persons:            
            ans.append(bit.point_query(m[p]))
        return ans
        



if __name__=="__main__":
    flowers = [[1,6],[3,7],[9,12],[4,13]]; persons = [2,3,7,11]
    print(Solution().fullBloomFlowers(flowers, persons))
    print(Solution().fullBloomFlowers2(flowers, persons))
    flowers = [[1,10],[3,3]]; persons = [3,3,2]
    print(Solution().fullBloomFlowers(flowers, persons))
    print(Solution().fullBloomFlowers2(flowers, persons))
    flowers = [[19,37],[19,38],[19,35]]
    persons = [6,7,21,1,13,37,5,37,46,43]
    print(Solution().fullBloomFlowers(flowers, persons))
    print(Solution().fullBloomFlowers2(flowers, persons))
    flowers = [[880291966,885633462],[23061436,635154137],[525989415,942828015],[288624072,508917088],[113681737,920638241],[974421257,991106719],[593907280,773214044],[179742678,710585627],[224377033,838830641],[321993685,351677532],[842596552,897894542],[930392106,958560387],[134098427,358706487],[28551066,138119932],[237548636,782819183],[573382920,734129625],[684900987,966011731],[59759296,403877405],[391958557,825295616],[848001514,958985051],[468535757,918912510],[369664513,525940591],[966523124,981594042],[459524518,900060686],[496650774,943982810],[470564237,754099373],[44970861,896804460],[712788735,998918142],[68447291,656303561],[269546195,343242668],[254634548,608658420],[958780620,985614332],[266489112,535866620],[631160840,969273760],[476953509,913816608],[687554172,954953884],[583304541,585163521],[452424959,608832631],[176573066,542734084],[39458913,536061151],[740223715,935486506],[750982741,838247657],[974753276,975740415],[514404450,581137374],[717927313,975616578],[117195007,589767614],[798078731,894686195],[684729332,848921671],[224868382,503300031],[429190745,580831737],[68791438,696670090],[6294092,114497200],[223064168,503661321],[836201809,923656912],[651332200,747079117],[94407692,903089008],[678103367,865453734],[826850173,932779980],[107153345,702844505],[161960380,198230137],[917493076,921108821],[964193719,975913897],[888691440,978497517],[43863437,766383879],[875151855,911028950],[575023077,935019093],[824233060,871778133],[775482967,874568057],[947512807,974207078],[118627166,472309232],[109926647,542108654],[760734053,821300535],[737578727,896883730],[149445072,616336874],[819605817,838039353],[487062956,997477656],[439626854,886978643],[330695923,951735148],[41523308,54654190],[56665728,227398277],[1336191,699676608],[686786370,985490449],[610020284,756253549],[510937447,657759825],[271559173,737962145],[643591695,667916299],[551854208,796907273],[691690084,746084784],[311723668,780770173],[170644665,631673892],[178858060,949136139],[865929071,896214140],[733746649,870810909],[50083207,766719822],[1869674,942748277],[737843496,955817899]]
    persons = [873313443,159436501,159305437,736319765,349487165,927624344,312147038,370284373,225189318,916424721,649426944,167983882,867141569,187525223,572773839,107832244,36034463,418109112,995053388,115067788,355765717,754871579,226411736,400186539,674098476,212132094,89751279,197589093,94545319,304320445,386093486,466316859,771766280,365774702,855013183,722427788,779456258,454407767,934442710,1546181,35430407,893606729,837043722,630066442,861372301,826752901,343238347,507111334,688482269,964721564,5400758,239519578,726928426,510934289,28864319,452023285,648992676,15171978,134086839,961728796,952509096,928098081,660712985,505234066,352319621,107192501,189615591,835076144,335094716,520642976,786394277,421601724,685673549,31548631,464356092,546902224,598770012,780247084,801563337,837106458,897592215,970458671,794359161,328138150,83834801,630384141,251337746,144313322,40188151,243652680]
    print(Solution().fullBloomFlowers(flowers, persons))
    print(Solution().fullBloomFlowers2(flowers, persons))    
    flowers = [[1000000000,1000000000] for _ in range(5*10**4)]
    persons = [1000000000]*(5*10**4)
    Solution().fullBloomFlowers2(flowers, persons)
    # Solution().fullBloomFlowers(flowers, persons)

