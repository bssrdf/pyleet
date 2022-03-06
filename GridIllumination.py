'''

-Hard-

There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the 
lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or 
iagonal.

You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, 
determine whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off 
the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell 
shares either a side or corner with grid[rowj][colj].

Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was 
illuminated, or 0 if the lamp was not.

 

Example 1:


Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.

The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

Example 2:

Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
Output: [1,1]
Example 3:

Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
Output: [1,1,0]
 

Constraints:

1 <= n <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == 2
0 <= rowi, coli < n
queries[j].length == 2
0 <= rowj, colj < n

'''
from typing import List, Dict
from collections import defaultdict

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lampRow = defaultdict(set)
        lampCol = defaultdict(set)
        lampDiag = defaultdict(set)
        lampAntiDiag = defaultdict(set)
        lamps = set([(i,j) for i,j in lamps])
        res = [0]*len(queries)
        for i,j in lamps:
            lampRow[i].add((i,j))
            lampCol[j].add((i,j))
            lampDiag[i-j].add((i,j))
            lampAntiDiag[i+j].add((i,j))
        for i in range(len(queries)):
            x, y = queries[i]
            if len(lampRow[x]) > 0 or len(lampCol[y]) > 0 \
               or len(lampDiag[x-y]) or len(lampAntiDiag[x+y])> 0:
               res[i] = 1
            for i1 in range(-1,2):
                for j1 in range(-1,2):
                    lx, ly = x+i1, y+j1
                    if (lx, ly) in lamps:
                        lamps.remove((lx,ly)) 
                        lampRow[lx].remove((lx,ly))
                        lampCol[ly].remove((lx,ly))
                        lampDiag[lx-ly].remove((lx,ly))
                        lampAntiDiag[lx+ly].remove((lx,ly))
        return res

        

        

if __name__ == "__main__":
    n = 5; lamps = [[0,0],[4,4]]; queries = [[1,1],[1,0]]
    print(Solution().gridIllumination(n, lamps, queries))
    n = 5; lamps = [[0,0],[4,4]]; queries = [[1,1],[1,1]]
    print(Solution().gridIllumination(n, lamps, queries))
    n = 5; lamps = [[0,0],[0,4]]; queries = [[0,4],[0,1],[1,4]]
    print(Solution().gridIllumination(n, lamps, queries))
    n = 6; lamps = [[1,1]]; queries = [[2,0],[1,0]]
    print(Solution().gridIllumination(n, lamps, queries))
    n = 1000000000
    lamps = [[387854743,465038173],[490449559,984251395],[978965991,584336837],[362769976,936183641],[282026395,371304454],[60062259,338784634],[385123372,385935577],[557516523,176810777],[478440326,897025676],[61407350,323031998],[363234955,3035008],[563712799,736060484],[437924238,706738348],[90017253,50856796],[941474520,964655639],[149741817,181849609],[867790631,795095393],[36091972,280771107],[340759594,328435771],[862857694,309318356],[527336198,665719018],[745761432,321337629],[235955924,240733896],[371202675,488123986],[45424928,634763971],[272052007,137616026],[41814636,243912669],[377290397,65429872],[695685803,941998506],[18149237,198697509],[221408710,884203733],[433764737,264464475],[586380315,249430939],[69255240,680531083],[417777912,674264654],[463097732,569295488],[985680676,861713875],[542570916,112111578],[266462551,217856036],[222544971,485542029],[945684670,992550608],[688880335,310048095],[286482296,947258742],[127044795,141887597],[101944603,458031181],[40797773,712796582],[407954223,890025119],[895550713,242796366],[696469937,258815306],[406813156,877884029],[472766866,46815038],[831498345,854483870],[789233974,541162497],[951350424,151598320],[411996918,544388142],[826856882,814717192],[973110686,616253425],[403459246,794496845],[387396335,48480653],[7764664,708000891],[563297310,18321366],[451741100,851224865],[754898515,470208695],[456142495,465464867],[571010860,434412462],[962583639,649362744],[864479543,780607051],[67227598,72743277],[218619003,871288501],[739766963,132327328],[591712496,577699876],[755644392,756697349],[319818498,46635368],[585413637,771579301],[423699474,718143329],[944931796,382543066],[935571701,616505732],[499694803,112180693],[294824563,441197149],[548624309,381022232],[793601481,214995975],[454439137,325784572],[675944232,802646710],[525424369,807904045],[58392627,968144685],[682610997,188739369],[561068677,867520840],[170486830,597258692],[490002473,878930548],[158657555,86573478],[392983584,969745458],[224734031,762039499],[216765151,34918040],[921511168,916022530],[72309454,262788303],[451728250,194856047],[299659466,299650966],[176188099,85992970],[160737955,607337917],[600720148,922509854],[894672287,224828075],[441930590,230159050],[121062645,528934617],[288176578,198702211],[911291475,881131093],[163963416,90164880],[8129625,476603712],[59307113,286711181],[778528028,436004944],[973696885,558168041],[948362916,625509199],[292941102,577037928],[646867821,635146650],[42448187,84286625],[616513770,39474850],[93163894,984322944],[670072317,668933742],[244082799,790512070],[798397825,543070232],[300494310,833478788],[211354305,318369356],[967888212,976624036],[922288637,491784652],[992576611,326957664],[864613612,158599150],[429904754,986642889],[113530165,529395996],[418262034,877528385],[979490549,278285651],[868502923,220503809],[829767996,129954981],[639536984,600325780],[530594959,621888439],[343777190,986496346],[941123944,631158851],[559444441,436917510],[744902321,761174423],[327362824,485354017],[980976205,368515349],[155469436,743789188],[297816976,930902193],[717005365,876103138],[933000641,953327478],[128961893,943985724],[646506655,564652033],[395592946,556393578],[861382873,483769092],[725564920,12551321],[651433109,631275973],[887021637,767707848],[233999338,194867868],[430752988,486039882],[885357925,980206968],[947812467,643108166],[52051080,880523867],[481342452,486297402],[481881158,501951449],[957767936,178200436],[145161609,116686750],[292081255,597912216],[249391533,943847141],[375840433,920893981],[689957634,849366785],[103056536,71727311],[129050445,764407256],[894304140,304459087],[223778375,995425378],[130796078,626202254],[41756701,748490543],[476949717,801175126],[207013358,287195358],[741541900,350651329],[100904528,737998503],[638120721,941307327],[110747084,4976850],[497799256,892035477],[125570909,54846782],[262790151,46599001],[927442165,7709147],[595133047,258234999],[625608697,30545200],[724017337,162589743],[444090304,104498390],[659044623,970519572],[386707479,631592442],[534718830,447505550],[741396416,834400735],[745768963,579074393],[534324974,635421786],[678451627,301692932],[86706634,466676308],[177906809,241779315],[35844850,115907660],[75794484,19268446],[579072501,326571218],[44555990,541274320],[847969752,556364045],[625992974,446025896],[10635668,876778294],[680181951,656598811],[890751125,30595355],[111128959,272516912],[921898812,749743773],[922384665,822810434],[836231518,171845682],[205422603,383082370],[950809796,912698723],[285326344,201783411],[683105705,279828815],[131224696,445927276],[886153023,644456743],[489238771,99717402],[600682026,686093488],[318518218,563031547],[812342531,342556868],[586709630,690708195],[576990422,696892881],[470556231,738973563],[820881828,66976856],[674543758,131584189],[887013602,158765935],[530766707,192316282],[419162616,243923264],[636756040,993263828],[470558404,542996360],[156634131,193317572],[698521108,155131929],[69904400,405444757],[839854127,547461464],[458404397,592938855],[211116877,579833023],[630843277,450283693],[150521370,649518940],[312582,791065775],[588045879,852950609],[253960610,786406153],[76199097,667540306],[195475234,3403562],[562323112,266231082],[1635958,29867222],[903833985,627314742],[76196422,75136165],[981691829,955902696],[45309804,215065217],[638156584,667344965],[997463928,551337004],[406842803,130989672],[622242091,146652600],[812252578,815585533],[330081020,213675533],[460897334,16966598],[408997782,538811238],[994330148,892558106],[744624728,284813268],[627815444,646655585],[915728851,75636154],[375436067,713282201],[801281616,327151695],[662652769,37589716],[970769992,143151647],[741264468,312654520],[27380457,283472266],[937681779,936215293],[450388120,778275652],[599394476,112418290],[935225194,137485523],[406707423,186407417],[107182505,369235732],[601181793,121976327],[992103509,787053751],[289897850,859607589],[559472032,640702142],[416492263,430994929],[279229297,194407170],[799864920,488130334],[88183778,168580270],[983594739,595884527],[641767362,898761922],[406317520,154220992],[776290580,244276369],[688290938,337772413],[41091470,413307971],[242051956,431736361],[287849243,505716564],[47798962,65181529],[644189274,540760851],[122882588,303312822],[196756764,803613476],[405885455,670663039],[195940074,639545855],[197354971,502135556],[309625724,103212398],[410582598,950677804],[629788483,59196691],[534038535,25753072],[274960864,471527136],[224808012,847928030],[526423722,132256668],[939132724,37573527],[646414637,517905765],[919142998,504457809],[800497062,573994537],[481508665,988727381],[128595336,497955371],[88352729,376557186],[142759417,816422021],[713915177,309106632],[686318677,912339360],[158711179,602252206],[814559402,18852285],[366957401,725055181],[209006139,423624559],[188480352,331301715],[608013310,844307487],[277393248,512118657],[530737950,184520327],[166088845,338025517],[336816505,899782967],[233077777,169088321],[711290914,324133652],[236302216,307816506],[884902880,758844884],[518963586,273989290],[343404974,219515523],[823047172,818794166],[441256761,192196096],[619922695,632827288],[943477093,33043328],[366617848,132828702],[323504328,93533451],[79043895,73804073],[94791214,29054458],[554166936,6704],[91510547,590144895],[648371172,801645498],[230270508,406347549],[194138201,398228967],[803725278,852683052],[781064230,734393064],[899210949,642066263],[912142064,251724163],[825549871,443376925],[908964432,962629520],[900907167,900081235],[493837395,927539326],[611045962,612564384],[303881720,125009870],[486974365,5853951],[739278262,859302295],[267934645,176711745],[999105523,417952513],[698602725,488796552],[896803726,686364362],[74148660,150694350],[758981206,256913860],[728124124,229643612],[974827408,300682068],[371427532,434879571],[559498357,463488501],[6251303,899300646],[616652977,509233587],[713150915,172371230],[132059878,919205041],[652465835,50891477],[646527271,244555171],[195707038,410200763],[963469181,745885781],[985127821,803197333],[135707749,950740002],[163283745,329123576],[128954192,399038077],[461817138,285114834],[401916706,416135020],[474814033,712844514],[307582644,407545863],[340932671,524760379],[352005459,89256190],[600135796,471214277],[108615486,554688273],[745708697,504506044],[576682027,268155797],[709027086,931903535],[743603650,753779446],[674733925,184572546],[654708257,924376879],[956024549,43202540],[167637078,459883603],[451576072,368951802],[466522344,117562120],[42458621,798412810],[775497295,751550727],[529035558,11076561],[282597751,865519006],[269425563,550261206],[860475458,926152237],[220197030,930032116],[135158787,716525228],[932046405,642675676],[130983427,619245092],[78995372,739316625],[355168255,235476785],[194923968,78680042],[338189480,948642951],[814269852,955313427],[581012002,361452394],[667924240,389650188],[881046149,349566516],[35513629,92619817],[230487647,160988883],[64439930,971477392],[995725105,254132040],[393717778,247596990],[682270189,308287017],[227539844,539231490],[574189439,11921695],[342595490,830823425],[197006657,277303145],[171622130,170726960],[133058948,448916056],[294199856,614797917],[842907150,489580497],[237842634,233239847],[913614999,385329870],[647898978,326152577],[407163723,858030045],[497555024,414619443],[596442955,436090783],[804484638,977878361],[123010859,714711370],[82311690,37944546],[234632054,452778792],[429864071,536937746],[824363814,62379798],[819921340,247350784],[51443244,397183750],[820057091,731396377],[55618030,842263933],[997942891,709358491],[94723011,583451157],[93578551,553552667],[971561337,526347772],[570496093,964198400],[302976464,531566196],[535639560,840194053],[107527421,63146321],[695509271,496593083],[243850536,966261630],[490016156,256262660],[380174062,234583416],[2286941,793046169],[935603679,953165777],[141713494,85653638],[651268865,507187630],[402440500,80295849],[332000075,723732810],[792369628,590214198],[116873771,132716145],[437011938,366316853],[826358785,632394502],[966389010,942032642],[545518753,883033981],[399736811,318508493],[458243541,245549409],[888878623,745001496],[773599193,41453007],[989774101,761090876],[518680029,182334458],[855990375,641530852],[189281927,795855781],[971576932,150645903],[225954926,680919468],[424088207,193352722],[286286496,624176251],[217686046,151713300],[342614813,562990229],[812082300,131883921],[201708377,898283790],[648890311,28104024],[628383934,404735506],[344551762,234252941],[108636456,916634972],[96835621,888375591],[361482599,56433855],[719862648,114503283],[130965952,988516513],[275688764,369195919],[988758637,154149499],[654898322,13741040],[786458136,896579930],[92258385,531354589],[935268964,150978657],[749705604,883258097],[870088292,598487365],[783946730,526272669],[997980962,22962383],[43488885,131215523],[701773850,43633502],[91339723,652001692],[975178684,852013922],[615356104,142262131],[447173101,996508130],[697231098,29344232],[396785798,392155895],[321041188,480548623],[958065620,699868751],[845695419,764739534],[964663062,737062315],[433859436,393219170],[545150211,692022625],[556506516,830278362],[907361345,992117978],[786702022,651102106],[554899951,791525141],[240949577,184589786],[867157532,494737699],[663300503,584071205],[297371213,760383145],[275647712,547845851],[32985083,857327713],[879799173,477692079],[912802066,399635097],[515182493,156413737],[210358900,861744050],[706162035,271471908],[909791348,811948706],[63907845,49249617],[192980316,11706227],[615942023,183594163],[883946983,968678850],[780999646,20263202],[430507975,157366592],[262654758,57232328],[864484384,233447988],[543822381,458247590],[989642251,191651320],[642932981,298583568],[421624084,397907832],[784944438,93154605],[665584573,218397622],[916738265,337902712],[803019257,898313800],[68799102,823965506],[571250609,785737688],[389551607,15753517],[132027203,845392547],[651732171,630636210],[73349118,306087675],[784537780,499776924],[106267815,944693189],[448264225,910173067],[726911478,575260412],[327680693,376708211],[754178330,985710636],[275005894,576193818],[860125233,725955319],[83914975,737682333],[907308753,415037844],[433190462,982393835],[497826946,407639883],[453834582,547227208],[231728450,735719162],[347619151,600444876],[418338303,377445779],[792041857,136578786],[86692128,591849628],[725785597,193946569],[859931389,306412717],[595706372,656463126],[803270242,992537589],[139981965,13143088],[68734736,587419830],[269936835,748463571],[555575868,242320837],[982771845,50273422],[406829839,42528523],[323462885,503058757],[889116964,940269062],[337036970,833303983],[463634188,88893000],[168429773,34514137],[627283149,875185143],[937279231,622829985],[711844959,896705100],[853877282,748863291],[648905262,624735764],[312649420,769798576],[849159579,287236658],[276369351,730677850],[959648635,807047195],[352536211,379982442],[398679702,481442904],[987969507,940404066],[941549097,654635784],[387931164,758082971],[165356645,877105755],[972071897,661521601],[517382893,789568280],[760930409,628886609],[526043996,250641688],[432855119,886289954],[253110205,924567496],[438374850,168162009],[846510353,433785515],[295200043,754244723],[66061773,647088086],[614876073,302888639],[365728857,354805875],[63092112,759322593],[30032274,945337150],[408100581,148698321],[194509640,937667851],[625514468,866890714],[97705665,349191998],[976286075,205645595],[845345076,615005777],[897973708,203838729],[34518607,793600081],[693557423,242215147],[435839666,653086050],[407183917,798646621],[816159858,240713271],[605181190,906898126],[600261527,415792794],[591684396,446158338],[338482334,868855274],[144776262,781225104],[209410807,303030168],[824643630,381576036],[243415432,133934505],[376021363,207935806],[898077992,88659255],[678565848,828748082],[976270117,582816496],[494998739,191195431],[430997439,586170261],[100389903,351018584],[325479082,800470652],[650857450,959228374],[653778320,743247375],[73936376,13978371]]
    queries = [[771666061,373149771],[70094718,648691736],[508060337,639059778],[832307703,891876512],[928099969,964374937],[260109203,254323707],[437035127,608065803],[107974579,197898716],[907134845,529083108],[808245103,230886603],[442785654,481795718],[703156240,749940900],[328857526,158950376],[5997462,19594519],[66119556,881332753],[879927602,444961318],[356695711,525770658],[6248909,377451177],[995059126,655624522],[163310208,921195213],[358097647,297792079],[118896922,403873937],[886944865,895775500],[417756318,410576967],[949569177,521229677],[611698113,36350233],[952689945,585188724],[645327216,973942146],[900930773,411414968],[800051528,241859025],[159359668,356996577],[834518044,461510826],[113953813,276172589],[20618356,652589956],[92793671,644326126],[268515592,747950379],[209871887,228892426],[377054024,796758591],[161713702,131398778],[763516375,816840628],[170235321,522341323],[710538507,762541393],[20228583,784097184],[788779888,640616497],[715347783,22102829],[304060482,428472132],[157413983,778951870],[444006902,599248847],[16889902,113475118],[105147057,414647272],[761074851,159951216],[303307983,456660219],[390423843,161194250],[224885598,55632456],[312962311,535214741],[373993120,415471458],[897895963,709752639],[600358029,599125681],[208447265,473876552],[653396814,263938033],[335619148,11603848],[518081987,860741297],[503590341,510910440],[986605054,527393493],[138330666,548872676],[133232070,543840021],[381209354,765806096],[352810773,87556476],[409346922,55408528],[983847067,888584681],[177942595,638736542],[156283960,251927697],[799062273,882276615],[651365765,884485755],[550084101,8610478],[715960396,810173954],[988952356,718487560],[413322508,244198743],[11828263,110720159],[784282998,516754685],[471077705,203042192],[852763378,92933195],[760575420,242724876],[270254363,511699949],[384498724,968268250],[268088895,378428516],[356179738,969242067],[279983072,831359617],[796367274,755967077],[102181173,965162478],[757487573,65134098],[427636650,803949477],[817317136,767026670],[23019867,48971382],[503318724,757451811],[928367005,655558022],[957613260,123746928],[217813878,191117003],[453873145,952958630],[221263904,210311569],[878347921,825453866],[579548554,36388600],[158381772,728898423],[752900310,386400883],[278893910,976345241],[348594396,81171530],[960091600,70053810],[862063782,489158681],[896539983,92160120],[950922738,774216527],[87904476,346748341],[595688884,306896304],[431821298,473722822],[532928657,1491924],[365166338,844326173],[638831460,249922981],[328774642,338855615],[578568124,896458469],[853948058,5962439],[54906972,266083238],[855742278,382529761],[67520443,279671503],[253602615,638198480],[628281986,175769758],[147213090,344395496],[822530576,704582433],[750991791,757624468],[524403961,899424955],[73821691,277929681],[983378819,875611302],[339999254,719474353],[766097447,487723371],[451251078,951836634],[509661206,738412907],[883213763,952842501],[49292210,377471834],[265365177,391871103],[670565648,10451134],[37953353,519664811],[994277501,689677940],[138655687,468555389],[301548278,79127852],[248986237,26762752],[370811054,800904168],[226049063,211472594],[960826252,440240257],[598113398,904391331],[92184490,706109986],[218906253,759507898],[718277079,453031883],[405950855,661661551],[845298710,849965263],[195412719,532822706],[908843549,765099350],[800586053,424233091],[123499479,375722716],[689792640,393102967],[533594594,772467376],[727836807,2165050],[559084562,543060598]]
    print(Solution().gridIllumination(n, lamps, queries))
