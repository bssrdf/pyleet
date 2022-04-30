'''
-Medium-
*BFS*

You are given a 0-indexed integer array nums containing distinct numbers, an integer start, and an integer goal. There is an integer x that is initially set to start, and you want to perform operations on x such that it is converted to goal. You can perform the following operation repeatedly on the number x:

If 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:

x + nums[i]
x - nums[i]
x ^ nums[i] (bitwise-XOR)
Note that you can use each nums[i] any number of times in any order. Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.

Return the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible.

 

Example 1:

Input: nums = [2,4,12], start = 2, goal = 12
Output: 2
Explanation: We can go from 2 → 14 → 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12
Example 2:

Input: nums = [3,5,7], start = 0, goal = -4
Output: 2
Explanation: We can go from 0 → 3 → -4 with the following 2 operations. 
- 0 + 3 = 3
- 3 - 7 = -4
Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.
Example 3:

Input: nums = [2,8,16], start = 0, goal = 1
Output: -1
Explanation: There is no way to convert 0 into 1.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i], goal <= 109
0 <= start <= 1000
start != goal
All the integers in nums are distinct.


'''

from typing import List
from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        que = deque([(start,0)])       
        visited = set()        
        while que:
            x, steps = que.popleft()            
            for i in nums:
                for t in [x+i, x-i, x^i]:
                    if t == goal: return steps + 1
                    if 0 <= t <= 1000 and t not in visited:
                        visited.add(t)
                        que.append((t, steps+1))
        return -1

    



        


if __name__ == "__main__":
    print(Solution().minimumOperations(nums = [2,4,12], start = 2, goal = 12))
    print(Solution().minimumOperations(nums = [3,5,7], start = 0, goal = -4))
    print(Solution().minimumOperations(nums = [2,8,16], start = 0, goal = 1))
    nums = [-574083075,-393928592,-508025046,942818778,355796909,515245901,40297943,106087952,112856312,-516143616,363801856,431681353,726373078,947630603,357311001,594181298,-797268217,-741740009,310972287,588107527,-535699426,56324906,-77958073,739798122,-839472160,439902753,-599749231,-378067373,-466272504,-668036170,404827976,805486978,-762507067,726001618,-761047930,574054980,365793614,112020312,612806855,-256862366,174046424,646109365,263765015,952305939,864217737,-236873371,-991807014,365730786,-908194963,-778205177,-949314048,-636570500,-883257881,316313456,-846577965,132287864,-143230736,425542510,-99852882,-845180792,-329895545,402782707,-52191127,-470380017,-788836785,-655887976,-899430590,481923982,45348738,-595401481,-470990760,-417390352,-570278840,-873871723,-905595403,276201114,-733014032,126018863,452235438,-512574658,-172220362,845468743,-743189114,597319839,-584451932,410604481,-508885990,-670396751,-765996786,345814977,-920014372,-826696704,640912714,119494504,745808962,-503060001,-677959595,-831428592,282855843,150678167,-467803553,-503929808,636431692,-235369757,-964826080,93942566,-65314422,-385277528,-379647659,601981747,-724269861,-516713072,-487487495,655771565,406499531,-943540581,-290169291,438686645,-227355533,-822612523,218329747,-800810927,-944724740,-978181517,274815523,296317841,56043572,-712672386,-374759873,86973233,-246165119,73819230,-801140338,414767806,883318746,-822063159,-705772942,-674915800,710520717,-97115365,599549847,115344568,53002314,242487774,-665998906,-986068895,-844909606,-515222297,-500827406,317865850,-50395059,522417393,51184184,241544846,-996297136,-227251827,924359619,822815774,149467545,523511343,252991991,450254984,-393459583,617410075,197030479,-234418418,-256650708,872334551,779068346,216294504,-708680875,-171498970,-970211466,-176493993,729939373,-658054782,-342680218,75508900,-377139149,392008859,121412250,-163586626,-468148273,624248706,50004864,-862378428,-849927586,33598413,-157654824,-229712613,149116317,183820138,378717707,-995563605,777654910,511275580,-157964872,-718605034,-764316227,-225837302,-166208500,-587688677,78982205,-488693575,667205793,419165994,731543316,97551954,-387317666,-580873271,533504431,-31624036,-356035140,-849089082,-767376392,-625237600,940717947,-337709497,915255567,727274007,-879463448,-363148174,-854892492,110472344,-466194659,-146843198,-454944217,-365338018,-349424052,994474446,-554968068,-883734951,-697723265,583756420,-5696410,-413731452,-278706136,-399245668,83345207,-227231270,618384545,846514423,-556667092,590460194,-686116067,-509669269,-510065093,77094171,270317951,166095128,-918526061,-766370855,-20861321,478791777,663673443,-152055285,224745414,123998803,66824877,-85117337,212126175,-718523523,615359230,-212148589,620733736,-81197397,51814471,709312024,562145805,-770811828,321230393,-611636320,-421337549,-804527290,-416739656,-886764000,170695026,414273830,-449987380,-56782953,772039002,-961265403,-896009751,-524231358,497253209,-507048459,-308522246,-508249054,-53240581,-241704483,-974133571,232897679,-152365934,-861310248,-305766289,340680726,844612779,-180227470,40798478,729446447,395975250,-142447074,-606021375,47555730,294446347,452346091,-409427076,-845574381,-838995437,45787728,714700474,-315824001,694717388,502723269,119244099,-538412679,-207297135,-189078560,-812610469,-350061253,-73975237,-119323509,791863263,741180208,740488891,-475394166,-191585617,-441527154,767292531,201222965,-150196525,588513813,245328283,396662663,100705864,126789247,487161165,-460512081,-469521559,-998848254,-917609155,314537168,418002454,-926920818,-628671538,179971032,-105401559,449618919,823404672,178494651,-773108884,10686795,-506642993,-60172121,-510142552,651623281,-163851428,158562600,-782456228,-336697076,-571952851,849878818,-456510759,-65997243,-506043404,-558981572,186946604,124948039,954065944,707437320,-224056616,-319237038,512138196,742466011,-49725596,-784781640,-753413026,-331602365,-246166733,-658650959,-4888181,-547553549,786689548,-866846384,-212028209,-98029403,-325422497,-409855095,320083382,-491251215,-471713326,890922019,-766590943,-481641953,-227197451,-709166930,-965945544,407688175,-78385698,-372800469,389036825,79885300,-858488452,-390177477,233839191,-518116358,420408256,872470025,241770824,-106901417,-328631191,548580365,-88408815,-647601013,658880218,-870455388,277154380,370022702,-381519264,-800726224,183685380,208169777,925905330,732494840,251754641,-681988029,593628349,153852085,353590607,242118102,-788094641,-242801844,474214244,579450364,580046580,-269927114,249739292,295331955,-544556236,-814569172,808895922,707421114,305101587,621173158,-248896453,988552702,-375313331,-87289858,-796466539,-529411285,-197315984,33984203,-122839651,-90735568,277265491,762059774,-628018119,-406508643,-856856769,364613737,59319066,614382155,-614620718,-133957131,-394985422,-29943491,154443077,-72727846,392096990,562681453,364248049,-156700958,717335155,-343408748,77301840,-155372684,-432114609,414752267,-485732822,876096548,842614035,-614245110,-872219121,291509502,334817026,214330487,405297459,-449582485,789314834,936409758,452350380,-146649749,898255045,116506422,671728835,280507922,-189039799,-565803074,-439924663,-14345985,-98428526,57303809,424685389,-84977856,-9251973,998935249,229402894,-405424548,448394272,182149207,-728030940,347577568,567511928,-27655302,400866779,-509269521,-580602375,405956020,-855173313,258091129,909162200,-315251598,-236890006,-531780379,342955474,-65890269,-111521851,-139906773,34939329,927781348,300458386,-603518159,341287362,-234266006,634183737,454833275,79631354,-954691672,102295826,688738167,-958428411,-293858940,480440548,590037773,-365477625,-425165732,170388756,164258145,-507355122,44132561,982798160,-101120201,-920959602,-239250887,534862084,-834736952,-123162323,389682556,656996523,864481760,381156936,129520066,-995551618,106129054,-471580461,856850511,653020333,531769579,-190375506,-992983956,73867968,-931909584,403329114,-945055546,627782991,-666011011,214665550,505169020,210703185,-591690068,11218620,790987020,561646751,-33552011,-407054835,-850936697,-838201457,-878394038,-759131062,-857347819,531582062,941614352,-743754869,650338718,178603580,-834368178,-976933957,138667533,746471721,551579035,-173400777,-1191455,320121832,-756997945,402594806,934711944,970489131,-193223639,276816990,842959026,-799673669,-367385466,681433973,468892554,-455199860,393993101,905435993,218314965,284795080,913357885,-652530417,743455659,869345718,808902357,829820413,7206928,544900359,225903242,-507688526,750219353,-663810717,-643969173,-269151675,348252329,-144351998,693995296,-692546103,869432378,650161259,568234384,710782517,179157604,-446849233,-922615096,-61183498,30945194,819052356,467911324,119876349,46908453,-420671619,344944591,889080726,-619477633,174882730,553799129,-941691933,146036558,-116064711,222282163,-272996845,-147041859,-381977096,-786757040,229096334,712541239,326039628,-952490563,-362214129,-680530864,421358212,-472290821,-331398150,-42297937,-393141325,-467541333,655524006,452908624,-626562356,-758303565,338224482,312047704,599445442,-328430584,259549134,838272865,-755896597,-151000710,607787908,11870257,-680877184,528161590,769242561,-447486537,-127579653,135915595,-271181270,12536315,693445551,900639800,-692327759,-671179999,977783490,935798407,659688020,-478438023,-852131846,-900332354,-71029072,888095095,924175448,430392829,391195112,399460998,-173259008,-168543477,-495967896,-697314804,591126097,301126906,946273416,-772817341,-996445410,466876435,-92937212,-226599286,43831927,-588596503,-55759661,212885530,-805455693,572269060,415773175,-320900489,-651775079,5276363,91615150,-882588415,502210147,-401039810,26713405,-723806893,125439289,472777644,869504248,967552969,-268043646,-146710780,-511973692,-803204681,-146827180,-453201623,-878534466,631307563,507752930,-63646026,-348120807,222898965,-410732708,617953050,-478244422,877782569,-507956686,-196516478,-477074335,329039585,-480651334,-890030740,461391919,-977815738,-943937849,321402466,-588396975,-945139052,871313567,-484830305,365305963,891985414,466048577,880607400,-245705654,359506342,-612177301,840415132,693541406,707348310,971762025,-871678269,897143169,625100531,743908163,-315815019,-63211252,-962051459,510469141,566817231,-186207711,309838979,101194721,-127111899,-109107404,-702499174,918781433,34041307,927374088,-67369303,-680339659,202481166,-218771120,329951816,-280782626,-423403505,619779171,-567310903,-660420942,756801677,996208091,822990010,940351540,1331227,382201579,891956260,-894584436,346600029,805733487,-691767750,859030444,1]
    print(Solution().minimumOperations(nums, 938, 80))