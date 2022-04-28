'''

-Hard-


Alice had a 0-indexed array arr consisting of n positive integers. She chose an 
arbitrary positive integer k and created two new 0-indexed integer arrays lower 
and higher in the following manner:

lower[i] = arr[i] - k, for every index i where 0 <= i < n
higher[i] = arr[i] + k, for every index i where 0 <= i < n
Unfortunately, Alice lost all three arrays. However, she remembers the integers that 
were present in the arrays lower and higher, but not the array each integer belonged to. 
Help Alice and recover the original array.

Given an array nums consisting of 2n integers, where exactly n of the integers 
were present in lower and the remaining in higher, return the original array arr. 
In case the answer is not unique, return any valid array.

Note: The test cases are generated such that there exists at least one valid array arr.

 

Example 1:

Input: nums = [2,10,6,4,8,12]
Output: [3,7,11]
Explanation:
If arr = [3,7,11] and k = 1, we get lower = [2,6,10] and higher = [4,8,12].
Combining lower and higher gives us [2,6,10,4,8,12], which is a permutation of nums.
Another valid possibility is that arr = [5,7,9] and k = 3. In that case, lower = [2,4,6] and higher = [8,10,12]. 
Example 2:

Input: nums = [1,1,3,3]
Output: [2,2]
Explanation:
If arr = [2,2] and k = 1, we get lower = [1,1] and higher = [3,3].
Combining lower and higher gives us [1,1,3,3], which is equal to nums.
Note that arr cannot be [1,3] because in that case, the only possible way to obtain [1,1,3,3] is with k = 0.
This is invalid since k must be positive.
Example 3:

Input: nums = [5,435]
Output: [220]
Explanation:
The only possible combination is arr = [220] and k = 215. Using them, we get lower = [5] and higher = [435].
 

Constraints:

2 * n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 109
The test cases are generated such that there exists at least one valid array arr.


'''

from typing import List
from collections import Counter
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        # 
        n = len(nums) // 2 
        n2 = 2*n
        A = nums
        nums.sort()        
        for i in range(1, n*2):
            k = nums[i] - nums[0]
            if k != 0 and k % 2 == 0:         
                k2 = k//2 
                l, h = 0, 0                
                mark = [False]*n2                
                ans = []
                while l < n2 and h < n2:
                    while l < n2 and mark[l]:
                        l += 1
                    if l >= n2: break
                    mark[l] = True
                    while h < n2 and (mark[h] or A[h] != A[l]+k):
                        h += 1
                    if h >= n2: break
                    mark[h] = True
                    ans.append(A[l]+k2) 
                if len(ans) == n:
                    return ans
        return []

    def recoverArray2(self, nums: List[int]) -> List[int]:
        def check(nums, k):
            cnt, ans = Counter(nums), []
            for num in nums:
                if cnt[num] == 0: continue
                if cnt[num + k] == 0: return False, []
                cnt[num] -= 1
                cnt[num + k] -= 1
                ans += [num + k//2]
            return True, ans
            
        nums = sorted(nums)
        n = len(nums)
        for i in range(1, n):
            k = nums[i] - nums[0]
            if k != 0 and k % 2 == 0:
                a, b = check(nums, k)
                if a: return b
        
        
                   

if __name__ == "__main__":
    # print(Solution().recoverArray(nums = [2,10,6,4,8,12]))
    print(Solution().recoverArray(nums = [1,1,3,3]))
    print(Solution().recoverArray(nums = [5,435]))
    print(Solution().recoverArray(nums = [11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9]))
    print(Solution().recoverArray(nums = [2,9,4,6,6,5,4,5,4,8,7,10,6,8,2,3,11,5,3,8]))
    
    nums = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,204,206,208,210,212,214,216,218,220,222,224,226,228,230,232,234,236,238,240,242,244,246,248,250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324,326,328,330,332,334,336,338,340,342,344,346,348,350,352,354,356,358,360,362,364,366,368,370,372,374,376,378,380,382,384,386,388,390,392,394,396,398,400,402,404,406,408,410,412,414,416,418,420,422,424,426,428,430,432,434,436,438,440,442,444,446,448,450,452,454,456,458,460,462,464,466,468,470,472,474,476,478,480,482,484,486,488,490,492,494,496,498,500,502,504,506,508,510,512,514,516,518,520,522,524,526,528,530,532,534,536,538,540,542,544,546,548,550,552,554,556,558,560,562,564,566,568,570,572,574,576,578,580,582,584,586,588,590,592,594,596,598,600,602,604,606,608,610,612,614,616,618,620,622,624,626,628,630,632,634,636,638,640,642,644,646,648,650,652,654,656,658,660,662,664,666,668,670,672,674,676,678,680,682,684,686,688,690,692,694,696,698,700,702,704,706,708,710,712,714,716,718,720,722,724,726,728,730,732,734,736,738,740,742,744,746,748,750,752,754,756,758,760,762,764,766,768,770,772,774,776,778,780,782,784,786,788,790,792,794,796,798,800,802,804,806,808,810,812,814,816,818,820,822,824,826,828,830,832,834,836,838,840,842,844,846,848,850,852,854,856,858,860,862,864,866,868,870,872,874,876,878,880,882,884,886,888,890,892,894,896,898,900,902,904,906,908,910,912,914,916,918,920,922,924,926,928,930,932,934,936,938,940,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024,1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056,1058,1060,1062,1064,1066,1068,1070,1072,1074,1076,1078,1080,1082,1084,1086,1088,1090,1092,1094,1096,1098,1100,1102,1104,1106,1108,1110,1112,1114,1116,1118,1120,1122,1124,1126,1128,1130,1132,1134,1136,1138,1140,1142,1144,1146,1148,1150,1152,1154,1156,1158,1160,1162,1164,1166,1168,1170,1172,1174,1176,1178,1180,1182,1184,1186,1188,1190,1192,1194,1196,1198,1200,1202,1204,1206,1208,1210,1212,1214,1216,1218,1220,1222,1224,1226,1228,1230,1232,1234,1236,1238,1240,1242,1244,1246,1248,1250,1252,1254,1256,1258,1260,1262,1264,1266,1268,1270,1272,1274,1276,1278,1280,1282,1284,1286,1288,1290,1292,1294,1296,1298,1300,1302,1304,1306,1308,1310,1312,1314,1316,1318,1320,1322,1324,1326,1328,1330,1332,1334,1336,1338,1340,1342,1344,1346,1348,1350,1352,1354,1356,1358,1360,1362,1364,1366,1368,1370,1372,1374,1376,1378,1380,1382,1384,1386,1388,1390,1392,1394,1396,1398,1400,1402,1404,1406,1408,1410,1412,1414,1416,1418,1420,1422,1424,1426,1428,1430,1432,1434,1436,1438,1440,1442,1444,1446,1448,1450,1452,1454,1456,1458,1460,1462,1464,1466,1468,1470,1472,1474,1476,1478,1480,1482,1484,1486,1488,1490,1492,1494,1496,1498,1500,1502,1504,1506,1508,1510,1512,1514,1516,1518,1520,1522,1524,1526,1528,1530,1532,1534,1536,1538,1540,1542,1544,1546,1548,1550,1552,1554,1556,1558,1560,1562,1564,1566,1568,1570,1572,1574,1576,1578,1580,1582,1584,1586,1588,1590,1592,1594,1596,1598,1600,1602,1604,1606,1608,1610,1612,1614,1616,1618,1620,1622,1624,1626,1628,1630,1632,1634,1636,1638,1640,1642,1644,1646,1648,1650,1652,1654,1656,1658,1660,1662,1664,1666,1668,1670,1672,1674,1676,1678,1680,1682,1684,1686,1688,1690,1692,1694,1696,1698,1700,1702,1704,1706,1708,1710,1712,1714,1716,1718,1720,1722,1724,1726,1728,1730,1732,1734,1736,1738,1740,1742,1744,1746,1748,1750,1752,1754,1756,1758,1760,1762,1764,1766,1768,1770,1772,1774,1776,1778,1780,1782,1784,1786,1788,1790,1792,1794,1796,1798,1800,1802,1804,1806,1808,1810,1812,1814,1816,1818,1820,1822,1824,1826,1828,1830,1832,1834,1836,1838,1840,1842,1844,1846,1848,1850,1852,1854,1856,1858,1860,1862,1864,1866,1868,1870,1872,1874,1876,1878,1880,1882,1884,1886,1888,1890,1892,1894,1896,1898,1900,1902,1904,1906,1908,1910,1912,1914,1916,1918,1920,1922,1924,1926,1928,1930,1932,1934,1936,1938,1940,1942,1944,1946,1948,1950,1952,1954,1956,1958,1960,1962,1964,1966,1968,1970,1972,1974,1976,1978,1980,1982,1984,1986,1988,1990,1992,1994,1996,1998,5000,100002,100004,100006,100008,100010,100012,100014,100016,100018,100020,100022,100024,100026,100028,100030,100032,100034,100036,100038,100040,100042,100044,100046,100048,100050,100052,100054,100056,100058,100060,100062,100064,100066,100068,100070,100072,100074,100076,100078,100080,100082,100084,100086,100088,100090,100092,100094,100096,100098,100100,100102,100104,100106,100108,100110,100112,100114,100116,100118,100120,100122,100124,100126,100128,100130,100132,100134,100136,100138,100140,100142,100144,100146,100148,100150,100152,100154,100156,100158,100160,100162,100164,100166,100168,100170,100172,100174,100176,100178,100180,100182,100184,100186,100188,100190,100192,100194,100196,100198,100200,100202,100204,100206,100208,100210,100212,100214,100216,100218,100220,100222,100224,100226,100228,100230,100232,100234,100236,100238,100240,100242,100244,100246,100248,100250,100252,100254,100256,100258,100260,100262,100264,100266,100268,100270,100272,100274,100276,100278,100280,100282,100284,100286,100288,100290,100292,100294,100296,100298,100300,100302,100304,100306,100308,100310,100312,100314,100316,100318,100320,100322,100324,100326,100328,100330,100332,100334,100336,100338,100340,100342,100344,100346,100348,100350,100352,100354,100356,100358,100360,100362,100364,100366,100368,100370,100372,100374,100376,100378,100380,100382,100384,100386,100388,100390,100392,100394,100396,100398,100400,100402,100404,100406,100408,100410,100412,100414,100416,100418,100420,100422,100424,100426,100428,100430,100432,100434,100436,100438,100440,100442,100444,100446,100448,100450,100452,100454,100456,100458,100460,100462,100464,100466,100468,100470,100472,100474,100476,100478,100480,100482,100484,100486,100488,100490,100492,100494,100496,100498,100500,100502,100504,100506,100508,100510,100512,100514,100516,100518,100520,100522,100524,100526,100528,100530,100532,100534,100536,100538,100540,100542,100544,100546,100548,100550,100552,100554,100556,100558,100560,100562,100564,100566,100568,100570,100572,100574,100576,100578,100580,100582,100584,100586,100588,100590,100592,100594,100596,100598,100600,100602,100604,100606,100608,100610,100612,100614,100616,100618,100620,100622,100624,100626,100628,100630,100632,100634,100636,100638,100640,100642,100644,100646,100648,100650,100652,100654,100656,100658,100660,100662,100664,100666,100668,100670,100672,100674,100676,100678,100680,100682,100684,100686,100688,100690,100692,100694,100696,100698,100700,100702,100704,100706,100708,100710,100712,100714,100716,100718,100720,100722,100724,100726,100728,100730,100732,100734,100736,100738,100740,100742,100744,100746,100748,100750,100752,100754,100756,100758,100760,100762,100764,100766,100768,100770,100772,100774,100776,100778,100780,100782,100784,100786,100788,100790,100792,100794,100796,100798,100800,100802,100804,100806,100808,100810,100812,100814,100816,100818,100820,100822,100824,100826,100828,100830,100832,100834,100836,100838,100840,100842,100844,100846,100848,100850,100852,100854,100856,100858,100860,100862,100864,100866,100868,100870,100872,100874,100876,100878,100880,100882,100884,100886,100888,100890,100892,100894,100896,100898,100900,100902,100904,100906,100908,100910,100912,100914,100916,100918,100920,100922,100924,100926,100928,100930,100932,100934,100936,100938,100940,100942,100944,100946,100948,100950,100952,100954,100956,100958,100960,100962,100964,100966,100968,100970,100972,100974,100976,100978,100980,100982,100984,100986,100988,100990,100992,100994,100996,100998,101000,101002,101004,101006,101008,101010,101012,101014,101016,101018,101020,101022,101024,101026,101028,101030,101032,101034,101036,101038,101040,101042,101044,101046,101048,101050,101052,101054,101056,101058,101060,101062,101064,101066,101068,101070,101072,101074,101076,101078,101080,101082,101084,101086,101088,101090,101092,101094,101096,101098,101100,101102,101104,101106,101108,101110,101112,101114,101116,101118,101120,101122,101124,101126,101128,101130,101132,101134,101136,101138,101140,101142,101144,101146,101148,101150,101152,101154,101156,101158,101160,101162,101164,101166,101168,101170,101172,101174,101176,101178,101180,101182,101184,101186,101188,101190,101192,101194,101196,101198,101200,101202,101204,101206,101208,101210,101212,101214,101216,101218,101220,101222,101224,101226,101228,101230,101232,101234,101236,101238,101240,101242,101244,101246,101248,101250,101252,101254,101256,101258,101260,101262,101264,101266,101268,101270,101272,101274,101276,101278,101280,101282,101284,101286,101288,101290,101292,101294,101296,101298,101300,101302,101304,101306,101308,101310,101312,101314,101316,101318,101320,101322,101324,101326,101328,101330,101332,101334,101336,101338,101340,101342,101344,101346,101348,101350,101352,101354,101356,101358,101360,101362,101364,101366,101368,101370,101372,101374,101376,101378,101380,101382,101384,101386,101388,101390,101392,101394,101396,101398,101400,101402,101404,101406,101408,101410,101412,101414,101416,101418,101420,101422,101424,101426,101428,101430,101432,101434,101436,101438,101440,101442,101444,101446,101448,101450,101452,101454,101456,101458,101460,101462,101464,101466,101468,101470,101472,101474,101476,101478,101480,101482,101484,101486,101488,101490,101492,101494,101496,101498,101500,101502,101504,101506,101508,101510,101512,101514,101516,101518,101520,101522,101524,101526,101528,101530,101532,101534,101536,101538,101540,101542,101544,101546,101548,101550,101552,101554,101556,101558,101560,101562,101564,101566,101568,101570,101572,101574,101576,101578,101580,101582,101584,101586,101588,101590,101592,101594,101596,101598,101600,101602,101604,101606,101608,101610,101612,101614,101616,101618,101620,101622,101624,101626,101628,101630,101632,101634,101636,101638,101640,101642,101644,101646,101648,101650,101652,101654,101656,101658,101660,101662,101664,101666,101668,101670,101672,101674,101676,101678,101680,101682,101684,101686,101688,101690,101692,101694,101696,101698,101700,101702,101704,101706,101708,101710,101712,101714,101716,101718,101720,101722,101724,101726,101728,101730,101732,101734,101736,101738,101740,101742,101744,101746,101748,101750,101752,101754,101756,101758,101760,101762,101764,101766,101768,101770,101772,101774,101776,101778,101780,101782,101784,101786,101788,101790,101792,101794,101796,101798,101800,101802,101804,101806,101808,101810,101812,101814,101816,101818,101820,101822,101824,101826,101828,101830,101832,101834,101836,101838,101840,101842,101844,101846,101848,101850,101852,101854,101856,101858,101860,101862,101864,101866,101868,101870,101872,101874,101876,101878,101880,101882,101884,101886,101888,101890,101892,101894,101896,101898,101900,101902,101904,101906,101908,101910,101912,101914,101916,101918,101920,101922,101924,101926,101928,101930,101932,101934,101936,101938,101940,101942,101944,101946,101948,101950,101952,101954,101956,101958,101960,101962,101964,101966,101968,101970,101972,101974,101976,101978,101980,101982,101984,101986,101988,101990,101992,101994,101996,101998,105000]
    print(Solution().recoverArray(nums = nums))
    print(Solution().recoverArray2(nums = nums))
    # print(len(nums))
    nums = [1,999999,2,1000000,5,1000003,10,1000008,17,1000015,26,1000024,37,1000035,50,1000048,65,1000063,82,1000080,101,1000099,122,1000120,145,1000143,170,1000168,197,1000195,226,1000224,257,1000255,290,1000288,325,1000323,362,1000360,401,1000399,442,1000440,485,1000483,530,1000528,577,1000575,626,1000624,677,1000675,730,1000728,785,1000783,842,1000840,901,1000899,962,1000960,1025,1001023,1090,1001088,1157,1001155,1226,1001224,1297,1001295,1370,1001368,1445,1001443,1522,1001520,1601,1001599,1682,1001680,1765,1001763,1850,1001848,1937,1001935,2026,1002024,2117,1002115,2210,1002208,2305,1002303,2402,1002400,2501,1002499,2602,1002600,2705,1002703,2810,1002808,2917,1002915,3026,1003024,3137,1003135,3250,1003248,3365,1003363,3482,1003480,3601,1003599,3722,1003720,3845,1003843,3970,1003968,4097,1004095,4226,1004224,4357,1004355,4490,1004488,4625,1004623,4762,1004760,4901,1004899,5042,1005040,5185,1005183,5330,1005328,5477,1005475,5626,1005624,5777,1005775,5930,1005928,6085,1006083,6242,1006240,6401,1006399,6562,1006560,6725,1006723,6890,1006888,7057,1007055,7226,1007224,7397,1007395,7570,1007568,7745,1007743,7922,1007920,8101,1008099,8282,1008280,8465,1008463,8650,1008648,8837,1008835,9026,1009024,9217,1009215,9410,1009408,9605,1009603,9802,1009800,10001,1009999,10202,1010200,10405,1010403,10610,1010608,10817,1010815,11026,1011024,11237,1011235,11450,1011448,11665,1011663,11882,1011880,12101,1012099,12322,1012320,12545,1012543,12770,1012768,12997,1012995,13226,1013224,13457,1013455,13690,1013688,13925,1013923,14162,1014160,14401,1014399,14642,1014640,14885,1014883,15130,1015128,15377,1015375,15626,1015624,15877,1015875,16130,1016128,16385,1016383,16642,1016640,16901,1016899,17162,1017160,17425,1017423,17690,1017688,17957,1017955,18226,1018224,18497,1018495,18770,1018768,19045,1019043,19322,1019320,19601,1019599,19882,1019880,20165,1020163,20450,1020448,20737,1020735,21026,1021024,21317,1021315,21610,1021608,21905,1021903,22202,1022200,22501,1022499,22802,1022800,23105,1023103,23410,1023408,23717,1023715,24026,1024024,24337,1024335,24650,1024648,24965,1024963,25282,1025280,25601,1025599,25922,1025920,26245,1026243,26570,1026568,26897,1026895,27226,1027224,27557,1027555,27890,1027888,28225,1028223,28562,1028560,28901,1028899,29242,1029240,29585,1029583,29930,1029928,30277,1030275,30626,1030624,30977,1030975,31330,1031328,31685,1031683,32042,1032040,32401,1032399,32762,1032760,33125,1033123,33490,1033488,33857,1033855,34226,1034224,34597,1034595,34970,1034968,35345,1035343,35722,1035720,36101,1036099,36482,1036480,36865,1036863,37250,1037248,37637,1037635,38026,1038024,38417,1038415,38810,1038808,39205,1039203,39602,1039600,40001,1039999,40402,1040400,40805,1040803,41210,1041208,41617,1041615,42026,1042024,42437,1042435,42850,1042848,43265,1043263,43682,1043680,44101,1044099,44522,1044520,44945,1044943,45370,1045368,45797,1045795,46226,1046224,46657,1046655,47090,1047088,47525,1047523,47962,1047960,48401,1048399,48842,1048840,49285,1049283,49730,1049728,50177,1050175,50626,1050624,51077,1051075,51530,1051528,51985,1051983,52442,1052440,52901,1052899,53362,1053360,53825,1053823,54290,1054288,54757,1054755,55226,1055224,55697,1055695,56170,1056168,56645,1056643,57122,1057120,57601,1057599,58082,1058080,58565,1058563,59050,1059048,59537,1059535,60026,1060024,60517,1060515,61010,1061008,61505,1061503,62002,1062000,62501,1062499,63002,1063000,63505,1063503,64010,1064008,64517,1064515,65026,1065024,65537,1065535,66050,1066048,66565,1066563,67082,1067080,67601,1067599,68122,1068120,68645,1068643,69170,1069168,69697,1069695,70226,1070224,70757,1070755,71290,1071288,71825,1071823,72362,1072360,72901,1072899,73442,1073440,73985,1073983,74530,1074528,75077,1075075,75626,1075624,76177,1076175,76730,1076728,77285,1077283,77842,1077840,78401,1078399,78962,1078960,79525,1079523,80090,1080088,80657,1080655,81226,1081224,81797,1081795,82370,1082368,82945,1082943,83522,1083520,84101,1084099,84682,1084680,85265,1085263,85850,1085848,86437,1086435,87026,1087024,87617,1087615,88210,1088208,88805,1088803,89402,1089400,90001,1089999,90602,1090600,91205,1091203,91810,1091808,92417,1092415,93026,1093024,93637,1093635,94250,1094248,94865,1094863,95482,1095480,96101,1096099,96722,1096720,97345,1097343,97970,1097968,98597,1098595,99226,1099224,99857,1099855,100490,1100488,101125,1101123,101762,1101760,102401,1102399,103042,1103040,103685,1103683,104330,1104328,104977,1104975,105626,1105624,106277,1106275,106930,1106928,107585,1107583,108242,1108240,108901,1108899,109562,1109560,110225,1110223,110890,1110888,111557,1111555,112226,1112224,112897,1112895,113570,1113568,114245,1114243,114922,1114920,115601,1115599,116282,1116280,116965,1116963,117650,1117648,118337,1118335,119026,1119024,119717,1119715,120410,1120408,121105,1121103,121802,1121800,122501,1122499,123202,1123200,123905,1123903,124610,1124608,125317,1125315,126026,1126024,126737,1126735,127450,1127448,128165,1128163,128882,1128880,129601,1129599,130322,1130320,131045,1131043,131770,1131768,132497,1132495,133226,1133224,133957,1133955,134690,1134688,135425,1135423,136162,1136160,136901,1136899,137642,1137640,138385,1138383,139130,1139128,139877,1139875,140626,1140624,141377,1141375,142130,1142128,142885,1142883,143642,1143640,144401,1144399,145162,1145160,145925,1145923,146690,1146688,147457,1147455,148226,1148224,148997,1148995,149770,1149768,150545,1150543,151322,1151320,152101,1152099,152882,1152880,153665,1153663,154450,1154448,155237,1155235,156026,1156024,156817,1156815,157610,1157608,158405,1158403,159202,1159200,160001,1159999,160802,1160800,161605,1161603,162410,1162408,163217,1163215,164026,1164024,164837,1164835,165650,1165648,166465,1166463,167282,1167280,168101,1168099,168922,1168920,169745,1169743,170570,1170568,171397,1171395,172226,1172224,173057,1173055,173890,1173888,174725,1174723,175562,1175560,176401,1176399,177242,1177240,178085,1178083,178930,1178928,179777,1179775,180626,1180624,181477,1181475,182330,1182328,183185,1183183,184042,1184040,184901,1184899,185762,1185760,186625,1186623,187490,1187488,188357,1188355,189226,1189224,190097,1190095,190970,1190968,191845,1191843,192722,1192720,193601,1193599,194482,1194480,195365,1195363,196250,1196248,197137,1197135,198026,1198024,198917,1198915,199810,1199808,200705,1200703,201602,1201600,202501,1202499,203402,1203400,204305,1204303,205210,1205208,206117,1206115,207026,1207024,207937,1207935,208850,1208848,209765,1209763,210682,1210680,211601,1211599,212522,1212520,213445,1213443,214370,1214368,215297,1215295,216226,1216224,217157,1217155,218090,1218088,219025,1219023,219962,1219960,220901,1220899,221842,1221840,222785,1222783,223730,1223728,224677,1224675,225626,1225624,226577,1226575,227530,1227528,228485,1228483,229442,1229440,230401,1230399,231362,1231360,232325,1232323,233290,1233288,234257,1234255,235226,1235224,236197,1236195,237170,1237168,238145,1238143,239122,1239120,240101,1240099,241082,1241080,242065,1242063,243050,1243048,244037,1244035,245026,1245024,246017,1246015,247010,1247008,248005,1248003,249002,1249000,250001,1249999,251002,1251000,252005,1252003,253010,1253008,254017,1254015,255026,1255024,256037,1256035,257050,1257048,258065,1258063,259082,1259080,260101,1260099,261122,1261120,262145,1262143,263170,1263168,264197,1264195,265226,1265224,266257,1266255,267290,1267288,268325,1268323,269362,1269360,270401,1270399,271442,1271440,272485,1272483,273530,1273528,274577,1274575,275626,1275624,276677,1276675,277730,1277728,278785,1278783,279842,1279840,280901,1280899,281962,1281960,283025,1283023,284090,1284088,285157,1285155,286226,1286224,287297,1287295,288370,1288368,289445,1289443,290522,1290520,291601,1291599,292682,1292680,293765,1293763,294850,1294848,295937,1295935,297026,1297024,298117,1298115,299210,1299208,300305,1300303,301402,1301400,302501,1302499,303602,1303600,304705,1304703,305810,1305808,306917,1306915,308026,1308024,309137,1309135,310250,1310248,311365,1311363,312482,1312480,313601,1313599,314722,1314720,315845,1315843,316970,1316968,318097,1318095,319226,1319224,320357,1320355,321490,1321488,322625,1322623,323762,1323760,324901,1324899,326042,1326040,327185,1327183,328330,1328328,329477,1329475,330626,1330624,331777,1331775,332930,1332928,334085,1334083,335242,1335240,336401,1336399,337562,1337560,338725,1338723,339890,1339888,341057,1341055,342226,1342224,343397,1343395,344570,1344568,345745,1345743,346922,1346920,348101,1348099,349282,1349280,350465,1350463,351650,1351648,352837,1352835,354026,1354024,355217,1355215,356410,1356408,357605,1357603,358802,1358800,360001,1359999,361202,1361200,362405,1362403,363610,1363608,364817,1364815,366026,1366024,367237,1367235,368450,1368448,369665,1369663,370882,1370880,372101,1372099,373322,1373320,374545,1374543,375770,1375768,376997,1376995,378226,1378224,379457,1379455,380690,1380688,381925,1381923,383162,1383160,384401,1384399,385642,1385640,386885,1386883,388130,1388128,389377,1389375,390626,1390624,391877,1391875,393130,1393128,394385,1394383,395642,1395640,396901,1396899,398162,1398160,399425,1399423,400690,1400688,401957,1401955,403226,1403224,404497,1404495,405770,1405768,407045,1407043,408322,1408320,409601,1409599,410882,1410880,412165,1412163,413450,1413448,414737,1414735,416026,1416024,417317,1417315,418610,1418608,419905,1419903,421202,1421200,422501,1422499,423802,1423800,425105,1425103,426410,1426408,427717,1427715,429026,1429024,430337,1430335,431650,1431648,432965,1432963,434282,1434280,435601,1435599,436922,1436920,438245,1438243,439570,1439568,440897,1440895,442226,1442224,443557,1443555,444890,1444888,446225,1446223,447562,1447560,448901,1448899,450242,1450240,451585,1451583,452930,1452928,454277,1454275,455626,1455624,456977,1456975,458330,1458328,459685,1459683,461042,1461040,462401,1462399,463762,1463760,465125,1465123,466490,1466488,467857,1467855,469226,1469224,470597,1470595,471970,1471968,473345,1473343,474722,1474720,476101,1476099,477482,1477480,478865,1478863,480250,1480248,481637,1481635,483026,1483024,484417,1484415,485810,1485808,487205,1487203,488602,1488600,490001,1489999,491402,1491400,492805,1492803,494210,1494208,495617,1495615,497026,1497024,498437,1498435,499850,1499848,501265,1501263,502682,1502680,504101,1504099,505522,1505520,506945,1506943,508370,1508368,509797,1509795,511226,1511224,512657,1512655,514090,1514088,515525,1515523,516962,1516960,518401,1518399,519842,1519840,521285,1521283,522730,1522728,524177,1524175,525626,1525624,527077,1527075,528530,1528528,529985,1529983,531442,1531440,532901,1532899,534362,1534360,535825,1535823,537290,1537288,538757,1538755,540226,1540224,541697,1541695,543170,1543168,544645,1544643,546122,1546120,547601,1547599,549082,1549080,550565,1550563,552050,1552048,553537,1553535,555026,1555024,556517,1556515,558010,1558008,559505,1559503,561002,1561000,562501,1562499,564002,1564000,565505,1565503,567010,1567008,568517,1568515,570026,1570024,571537,1571535,573050,1573048,574565,1574563,576082,1576080,577601,1577599,579122,1579120,580645,1580643,582170,1582168,583697,1583695,585226,1585224,586757,1586755,588290,1588288,589825,1589823,591362,1591360,592901,1592899,594442,1594440,595985,1595983,597530,1597528,599077,1599075,600626,1600624,602177,1602175,603730,1603728,605285,1605283,606842,1606840,608401,1608399,609962,1609960,611525,1611523,613090,1613088,614657,1614655,616226,1616224,617797,1617795,619370,1619368,620945,1620943,622522,1622520,624101,1624099,625682,1625680,627265,1627263,628850,1628848,630437,1630435,632026,1632024,633617,1633615,635210,1635208,636805,1636803,638402,1638400,640001,1639999,641602,1641600,643205,1643203,644810,1644808,646417,1646415,648026,1648024,649637,1649635,651250,1651248,652865,1652863,654482,1654480,656101,1656099,657722,1657720,659345,1659343,660970,1660968,662597,1662595,664226,1664224,665857,1665855,667490,1667488,669125,1669123,670762,1670760,672401,1672399,674042,1674040,675685,1675683,677330,1677328,678977,1678975,680626,1680624,682277,1682275,683930,1683928,685585,1685583,687242,1687240,688901,1688899,690562,1690560,692225,1692223,693890,1693888,695557,1695555,697226,1697224,698897,1698895,700570,1700568,702245,1702243,703922,1703920,705601,1705599,707282,1707280,708965,1708963,710650,1710648,712337,1712335,714026,1714024,715717,1715715,717410,1717408,719105,1719103,720802,1720800,722501,1722499,724202,1724200,725905,1725903,727610,1727608,729317,1729315,731026,1731024,732737,1732735,734450,1734448,736165,1736163,737882,1737880,739601,1739599,741322,1741320,743045,1743043,744770,1744768,746497,1746495,748226,1748224,749957,1749955,751690,1751688,753425,1753423,755162,1755160,756901,1756899,758642,1758640,760385,1760383,762130,1762128,763877,1763875,765626,1765624,767377,1767375,769130,1769128,770885,1770883,772642,1772640,774401,1774399,776162,1776160,777925,1777923,779690,1779688,781457,1781455,783226,1783224,784997,1784995,786770,1786768,788545,1788543,790322,1790320,792101,1792099,793882,1793880,795665,1795663,797450,1797448,799237,1799235,801026,1801024,802817,1802815,804610,1804608,806405,1806403,808202,1808200,810001,1809999,811802,1811800,813605,1813603,815410,1815408,817217,1817215,819026,1819024,820837,1820835,822650,1822648,824465,1824463,826282,1826280,828101,1828099,829922,1829920,831745,1831743,833570,1833568,835397,1835395,837226,1837224,839057,1839055,840890,1840888,842725,1842723,844562,1844560,846401,1846399,848242,1848240,850085,1850083,851930,1851928,853777,1853775,855626,1855624,857477,1857475,859330,1859328,861185,1861183,863042,1863040,864901,1864899,866762,1866760,868625,1868623,870490,1870488,872357,1872355,874226,1874224,876097,1876095,877970,1877968,879845,1879843,881722,1881720,883601,1883599,885482,1885480,887365,1887363,889250,1889248,891137,1891135,893026,1893024,894917,1894915,896810,1896808,898705,1898703,900602,1900600,902501,1902499,904402,1904400,906305,1906303,908210,1908208,910117,1910115,912026,1912024,913937,1913935,915850,1915848,917765,1917763,919682,1919680,921601,1921599,923522,1923520,925445,1925443,927370,1927368,929297,1929295,931226,1931224,933157,1933155,935090,1935088,937025,1937023,938962,1938960,940901,1940899,942842,1942840,944785,1944783,946730,1946728,948677,1948675,950626,1950624,952577,1952575,954530,1954528,956485,1956483,958442,1958440,960401,1960399,962362,1962360,964325,1964323,966290,1966288,968257,1968255,970226,1970224,972197,1972195,974170,1974168,976145,1976143,978122,1978120,980101,1980099,982082,1982080,984065,1984063,986050,1986048,988037,1988035,990026,1990024,992017,1992015,994010,1994008,996005,1996003,998002,1998000]
    print(Solution().recoverArray(nums = nums))
    print(Solution().recoverArray2(nums = nums))
    # print(len(nums))