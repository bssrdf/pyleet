def lpsGenerator(needle):
	n = len(needle)
	i = 0
	j = 1
	lps = [0] * n 
	while j < n:
		if needle[j] == needle[i]:
			lps[j] = lps[j - 1] + 1
			j += 1
			i += 1
		else:
			if i == 0:
				j += 1
			else:
				i = lps[i] - 1
	return lps

def partialMatchTable(P):
    m = len(P)
    pt = [0]*m
    k = 0
    for q in range(1,m):                
        while k > 0 and P[k] != P[q]:
            k = pt[k-1] # note the difference from CLRS text which has k = pt[k]
        if P[k] == P[q]:
            k += 1
        pt[q] = k
    return pt

def KMP(haystack, needle):
    """
    Knuth Morris Pratt Algorithm
    Parameters:
    haystack (str): string to be searched
    needle (str): string to be found
    Returns:
    int: index where matched pattern begins in haystack or -1
    """
    h, n = len(haystack), len(needle)
    i = 0
    j = 0
    #lps = lpsGenerator(needle)
    lps = partialMatchTable(needle)
    print(lps)
    '''
    while i < h:
        print(i,j)
        print(" "*i+'|'+' '*(h-i))
        print(haystack)
        print(" "*(i+j)+needle)
        if haystack[i] == needle[j]:
            if j == n - 1:
                return i - n + 1 
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    '''
    for i in range(h):
        #print(i,j)
        print(" "*i+'|'+' '*(h-i))
        print(haystack)
        print(" "*(i-j)+needle)
        while j > 0 and needle[j] != haystack[i]:
            j = lps[j-1] # note the difference from CLRS text which has k = pt[k]
        if needle[j] == haystack[i]:
            j += 1
        if j == n:
            j = lps[j-1]
            return i-n+1 
    return -1


if __name__=="__main__":
    haystack = "BBC ABCDAB ABCDABCDABDE"
    #           "                   "
    needle   = "ABCDABD"
    print(KMP(haystack, needle))
    lps = partialMatchTable("ABCABCD")
    print(lps)
    lps = partialMatchTable("ABCDEABCDAB")
    print(lps)