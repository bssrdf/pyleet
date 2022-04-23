'''
-Hard-

*Segment Tree*

You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 

Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].
Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
k == queryCharacters.length == queryIndices.length
1 <= k <= 105
queryCharacters consists of lowercase English letters.
0 <= queryIndices[i] < s.length


'''

from typing import List

class SegmentTree:
    def __init__(self, data):
        self.nodes = [None] * 4 * len(data) #node: (value, left_node_index, right_node_index)
        self.data = data
        self._build_tree(0, 0, len(data)-1)

    def _left(self, index):
        return (index + 1) * 2 - 1

    def _right(self, index):
        return (index + 1) * 2

    def _build_tree(self, node_index, left_data_index, right_data_index):
        value = None
        if left_data_index == right_data_index:            
            # (longest c, longest len, prefix c, prefix len, suffix c, suffix len)
            
            # We need to keep tracking the 6 values in each segments.

            # longest repating character (noted as lc)
            # length of the above character (noted as ll)
            # longest repeating prefix character (noted as pc)
            # length of the above character (noted as pl)
            # longest repeating suffix character (noted as sc)
            # length of the above character (noted as sl)
            value = (
                self.data[left_data_index],
                1,
                self.data[left_data_index],
                1,
                self.data[left_data_index],
                1)
        else:
            left_node_index = self._left(node_index)
            right_node_index = self._right(node_index)

            mid_data_index = (left_data_index + right_data_index) // 2
            (left_lc, left_ll, left_pc, left_pl, left_sc, left_sl) = self._build_tree(left_node_index, left_data_index, mid_data_index)
            (right_lc, right_ll, right_pc, right_pl, right_sc, right_sl) = self._build_tree(right_node_index, mid_data_index + 1, right_data_index)
            
            lc = ll = None
            if left_ll > right_ll:
                lc = left_lc
                ll = left_ll
            else:
                lc = right_lc
                ll = right_ll
            if left_sc == right_pc and left_sl + right_pl > ll:
                ll = left_sl + right_pl
                lc = left_sc

            pc = left_pc
            pl = left_pl
            if left_pl == (mid_data_index - left_data_index + 1) and left_pc == right_pc:
                pl = left_pl + right_pl

            sc = right_sc
            sl = right_sl
            if right_sl == (right_data_index - mid_data_index) and left_sc == right_sc:
                sl = left_sl + right_sl
    
            value = (lc, ll, pc, pl, sc, sl)

        self.nodes[node_index] = value
        return value

    def _update(self, node_index, data_index, update_value, left_data_index, right_data_index):
        value = self.nodes[node_index]
        mid_data_index = (left_data_index + right_data_index) // 2
        left_node_index = self._left(node_index)
        right_node_index = self._right(node_index)

        new_value = None
        if left_data_index == right_data_index:
            new_value = (
                update_value,
                1,
                update_value,
                1,
                update_value,
                1)
        else:
            left_value = right_value = None
            if data_index <= mid_data_index:
                left_value = self._update(left_node_index, data_index, update_value, left_data_index, mid_data_index)
                right_value = self.nodes[right_node_index]
            else:
                left_value = self.nodes[left_node_index]
                right_value = self._update(right_node_index, data_index, update_value, mid_data_index + 1, right_data_index)
            (left_lc, left_ll, left_pc, left_pl, left_sc, left_sl) = left_value
            (right_lc, right_ll, right_pc, right_pl, right_sc, right_sl) = right_value
            
            lc = ll = None
            if left_ll > right_ll:
                lc = left_lc
                ll = left_ll
            else:
                lc = right_lc
                ll = right_ll
            if left_sc == right_pc and left_sl + right_pl > ll:
                ll = left_sl + right_pl
                lc = left_sc

            pc = left_pc
            pl = left_pl
            if left_pl == (mid_data_index - left_data_index + 1) and left_pc == right_pc:
                pl = left_pl + right_pl

            sc = right_sc
            sl = right_sl
            if right_sl == (right_data_index - mid_data_index) and left_sc == right_sc:
                sl = left_sl + right_sl
    
            new_value = (lc, ll, pc, pl, sc, sl)
        self.nodes[node_index] = new_value
        return new_value

    def update(self, data_index, update_value):
        self.data[data_index] = update_value
        return self._update(0, data_index, update_value, 0, len(self.data)-1)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(list(s))
        M = len(queryCharacters)
        ans = [0] * M
        for i in range(M):
            c = queryCharacters[i]
            p = queryIndices[i]
            st.update(p, c)
            ans[i] = st.nodes[0][1]
        return ans


if __name__ == "__main__":   
    print(Solution().longestRepeating(s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]))