import random

def quickselect_median(l):
    '''
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return  min(quickselect(l, len(l) / 2 - 1, pivot_fn),
                    quickselect(l, len(l) / 2, pivot_fn))
    '''
    #if len(l) % 2 == 1:
    return select(l, 0, len(l)-1, len(l) // 2)
    #else:
     #   return  min(select(l, 0, len(l) - 1, len(l) / 2 - 1 ),
      #              select(l, 0, len(l) - 1, len(l) / 2)



def partition(nums, p, r):
    x = nums[r]
    i = p-1
    for j in range(p,r):
        if nums[j] < x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1],nums[r] = nums[r], nums[i+1]    
    return i+1
        
def random_partition(nums,p,r):
    ri = random.randint(p,r)
    nums[ri], nums[r] = nums[r], nums[ri]
    return partition(nums, p, r) 

def select(nums, p, r, k):
    if p == r:
        return nums[p]
    q = random_partition(nums, p, r)
    i = q-p+1
    if i == k:
        return nums[q]
    elif k < i:
        return select(nums, p, q-1, k)
    else:
        return select(nums, q+1, r, k-i)

def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)