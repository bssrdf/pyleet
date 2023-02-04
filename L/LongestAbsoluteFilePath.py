# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:49:07 2017

@author: merli
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            print line
            name = line.lstrip('\t')
            depth = len(line) - len(name)     
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
            #print depth, name, pathlen
        return maxlen


if __name__ == "__main__":
    print Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    #Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")