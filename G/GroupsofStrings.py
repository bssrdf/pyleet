'''
-Hard-

You are given a 0-indexed array of strings words. Each string consists of lowercase 
English letters only. No letter occurs more than once in any string of words.

Two strings s1 and s2 are said to be connected if the set of letters of s2 can be 
obtained from the set of letters of s1 by any one of the following operations:

Adding exactly one letter to the set of the letters of s1.
Deleting exactly one letter from the set of the letters of s1.
Replacing exactly one letter from the set of the letters of s1 with any letter, 
including itself.
The array words can be divided into one or more non-intersecting groups. A string 
belongs to a group if any one of the following is true:

It is connected to at least one other string of the group.
It is the only string present in the group.
Note that the strings in words should be grouped in such a manner that a string 
belonging to a group cannot be connected to a string present in any other group. 
It can be proved that such an arrangement is always unique.

Return an array ans of size 2 where:

ans[0] is the maximum number of groups words can be divided into, and
ans[1] is the size of the largest group.
 

Example 1:

Input: words = ["a","b","ab","cde"]
Output: [2,3]
Explanation:
- words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2].
- words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2].
- words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1].
- words[3] is not connected to any string in words.
Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.  
Example 2:

Input: words = ["a","ab","abc"]
Output: [1,3]
Explanation:
- words[0] is connected to words[1].
- words[1] is connected to words[0] and words[2].
- words[2] is connected to words[1].
Since all strings are connected to each other, they should be grouped together.
Thus, the size of the largest group is 3.
 

Constraints:

1 <= words.length <= 2 * 104
1 <= words[i].length <= 26
words[i] consists of lowercase English letters only.
No letter occurs more than once in words[i].


'''
from typing import List
from collections import defaultdict,Counter

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # TLE: 82/97 test cases passed.
        n = len(words)
        bits = defaultdict(list)
        for i, word in enumerate(words):
            num = 0
            for c in word:
                num |= 1 << (ord(c)- ord('a'))
            bits[len(word)].append((num,i))
        roots = [i for i in range(n)]
        def find(x):
            while x != roots[x]:
                roots[x] = roots[roots[x]]
                x = roots[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                if fx < fy:
                    roots[fy] = fx
                else:
                    roots[fx] = fy
        lengths = sorted(bits.keys())
        for i in range(len(lengths)-1):
            arr = bits[lengths[i]]
            arr1 = bits[lengths[i+1]]
            for j in range(len(arr)):
                for k in range(j+1, len(arr)):
                    if lengths[i] == 1:
                        union(arr[j][1], arr[k][1])
                    elif bin(arr[j][0] & arr[k][0]).count('1') >= lengths[i]-1:
                        union(arr[j][1], arr[k][1])
            if lengths[i+1] == lengths[i]+1:
                for j in range(len(arr)):
                    for k in range(len(arr1)):
                        # print(lengths[i], words[arr[j][1]], bin(arr[j][0]), words[arr1[k][1]], bin(arr1[k][0]))
                        if arr[j][0] | arr1[k][0] == arr1[k][0]:                            
                            # print(lengths[i], words[arr[j][1]], bin(arr[j][0]), words[arr1[k][1]], bin(arr1[k][0]))
                            # print(lengths[i], arr[j][1], arr1[k][1], roots)
                            union(arr[j][1], arr1[k][1])
                            # print(lengths[i], arr[j][1], arr1[k][1], roots)

        arr = bits[lengths[len(lengths)-1]]
        for j in range(len(arr)):
            for k in range(j+1, len(arr)):
                if lengths[len(lengths)-1] == 1:
                    union(arr[j][1], arr[k][1])
                elif bin(arr[j][0] & arr[k][0]).count('1') >= lengths[len(lengths)-1]-1:
                    union(arr[j][1], arr[k][1])
        # prnt(roots)
        cnt = Counter()
        for i in range(n):
           cnt[find(i)] += 1
        # print(cnt)
        # k = 0
        # for j,root in enumerate(cnt):
        #     ws = []
        #     for i in range(n):
        #         if find(i) == root:   
        #             ws.append(words[i])
        #     k += len(ws)
        #     if len(ws) > 1:
        #        print(j+1,ws)
        # print('k = ', k, n)
        return [len(cnt), max(cnt.values())]

    def groupStrings3(self, words: List[str]) -> List[int]:
        
        w, n = words, len(words)        
        roots = [i for i in range(n)]
        ranks = [0]*n
        def find(x):
            while x != roots[x]:
                roots[x] = roots[roots[x]]
                x = roots[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                if ranks[fx] > ranks[fy]:
                    roots[fy] = fx
                else:
                    roots[fx] = fy
                    if ranks[fx] == ranks[fy]:
                        ranks[fy] += 1

        M = {sum(1<<(ord(i) - ord("a")) for i in word): j for j, word in enumerate(w)}

        masks = defaultdict(list)
        for idx, word in enumerate(w):
            vals = [ord(i) - ord("a") for i in word]
            mask = sum(1<<i for i in vals)
            for i in vals:
                masks[mask - (1<<i) + (1<<26)].append(idx)
                if mask - (1<<i) not in M: continue
                idx2 = M[mask - (1<<i)]
                union(idx, idx2)                
        for x in masks.values():
            for a, b in zip(x, x[1:]):
                union(a, b)
        
        cnt = Counter()
        for i in range(n):
           cnt[find(i)] += 1
        return [len(cnt), max(cnt.values())]
    
    def groupStrings2(self, w):
        M = {sum(1<<(ord(i) - ord("a")) for i in word): j for j, word in enumerate(w)}

        G = defaultdict(list)
        masks = defaultdict(list)
        for idx, word in enumerate(w):
            vals = [ord(i) - ord("a") for i in word]
            mask = sum(1<<i for i in vals)
            for i in vals:
                masks[mask - (1<<i) + (1<<26)].append(idx)
                if mask - (1<<i) not in M: continue
                idx2 = M[mask - (1<<i)]
                G[idx] += [idx2]
                G[idx2] += [idx]
        
        for x in masks.values():
            for a, b in zip(x, x[1:]):
                G[a] += [b]
                G[b] += [a]

        V, comps, r = set(), 0, 0
        col = []
        for u in range(len(w)):
            if u in V: continue            
            compsize, q = 1, [u]
            V.add(u)
            c = [w[u]]
            while q:
                u = q.pop()
                for v in G[u]:
                    if v in V: continue
                    compsize += 1
                    V.add(v)
                    q += [v]
                    c.append(w[v])
            col.append(c)
            r = max(r, compsize)
            comps += 1
        for c in col:
            if len(c) > 1:
                print(c)
        return [comps, r]



                    

            


if __name__ == "__main__":
    # print(Solution().groupStrings(words = ["a","b","ab","cde"]))    
    # print(Solution().groupStrings(words = ["a","ab","abc"]))  
    # print(Solution().groupStrings(words = ["qamp","am","khdrn"]))
    # print(Solution().groupStrings(words = ["ep","x","e","hj","sxru","vsbt","akwdp","q","vyle","lip"]))
    words = ["umeihvaq","ezflcmsur","ynikwecaxgtrdbu","u","q","gwrv","ftcuw","ocdgslxprzivbja","zqrktuepxs","cpqolvnwxz","geqis","xgfdazthbrolci","vwnrjqzsoepa","udzckgenvbsty","lpqcw","nekpvchqfgdo","iapjhxvdrmwetz","gw","waxokchnmifsruj","vqp","vbpkij","ufjvbstzh","swiu","knslbdcahfrox","ctofplkhednmv","g","zk","idretzjbpl","pxqdauys","mfgrqaktbzpv","vdtq","wyxjrcie","kl","jpcdzmli","oth","yumdawhfbskcjo","rvfksqhu","swemnvjpg","rnl","zgd","rmzdbcsqht","ure","qlusoaxprtebn","zkbmvtpya","jszxuwevfidkm","smlft","cpwugmbzfsqr","cblkjevhp","iyfnozaulex","qvlok","wsgm","du","awyplckj","aey","ycsjqnt","vtoqzsyx","ejqixsmrdhlofyp","kvlmurbzjg","lysdahgpwmrcn","af","jkezhdu","etjzqiyghdnovm","ycwdfnluoke","kwshbx","pyvaznljqwes","xakinu","e","zjexfgvhtabwcy","thuvwlnjkbxym","jorzeslpidmhubq","wnr","qzdv","qeovrbmwzgpdh","jkioenptaygfubh","bvndzxijope","cudizhjntbes","rnhzitpqoexwb","ihezcmfqouyl","q","mwtsdjqn","hrmc","hxaocbyikluvqsf","d","vgwjzuaondbcm","ibqxltf","rzyhguptmesqo","ruwgy","jvprwhtzuf","aupngodjexkiw","yhijelwpvtsrbqc","gtick","koilywcfbs","elv","dehxzlitskq","ptvbkql","msfxyjahlzo","oslxzfwrpmtyh","gypuchkwa","rsqij","tw","igbcylqfhtmjkr","nryhzjgi","pw","bnfairow","xjzrf","olxfypjtmrncuv","ifhue","akcvofuyzwbj","tvhxfeuiykpwbsz","wnrztclfpm","ozvypnfwrqg","cwkgr","gjyzrucplbsfe","pdtzmfoy","wehd","bnvqhcmg","uyw","sgynxljqbf","tvxbq","wcmguioelbdrkvx","okvtyexuj","hjbc","uidcswzm","jemtkvshizaub","rmb","jpgnqdemzcxa","dmalekhiyj","akocedu","rlpqufcv","r","lohgs","xapnorj","cdb","icopdtzxy","xcrflvojqgpkwt","elv","rp","yv","u","atdxqeilhkg","olfvmrgkb","rplxskabvtqmhw","n","rldswkyoujmfxpn","rvgejzdusoya","hvoft","wskgmjchz","luagnzkj","ywe","i","wcqtsk","umpvywknjbxacsd","ynavjpcrgq","jyftmklci","xfol","zh","kut","zvawyielscotkn","p","wykpqdjoz","uabtpxkvq","uabtifwhrvxc","sdcamqup","srghwfptloxvke","sfdywtx","tuohnxzjqmac","pwxjyhdurnfz","axgfcuqtiyhjz","rwqpyh","bmoznqavicdgp","jcu","vnkc","jpb","nvfqyahjkul","radpctwixygb","pvjmk","s","dzyqjbwucne","mgh","ivc","eaqc","yjimsadtcwbgk","lo","ayirlsfevtwpnd","wcsk","xlvejy","kcjrqf","a","ixsdga","vk","cqxyfotziwrvl","zmxboiewhfdjlnr","kdpwngf","zyretijxpw","ncw","ljw","mrxeciy","aqwcofnjypsgi","byuvhj","ukidyqzhxgowmc","cpqsmu","auwmcrpdisbzokg","pxgwmvfq","azgljrsyeqwxfic","xmlgpdrzwqe","emgdcqntjpwrf","hrwq","zmjkx","npabcide","dvlfxnt","kilqsvmborf","lvsxjnbimhpzfow","sqcym","tcjmkwq","yugkwdzvmteon","pq","nklmb","azqcnodkimtxve","ovpcfe","uqkcwjimbvdyx","xvdazh","xk"]
    print(Solution().groupStrings(words))
    print(Solution().groupStrings2(words))
    print(Solution().groupStrings3(words))