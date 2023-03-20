


nums = [2, 4, 5, 1, 3] 
A = nums                                
arr = [(v,i) for i,v in enumerate(nums)]
idx = [i for _,i in sorted(arr)]        
print('idx', idx)
ans = 0                                        
for i in range(len(idx)):               
    while idx[i] != i:                  
        j = idx[i]      
        print(idx[i], j, idx[j])   
        A[idx[i]], A[idx[j]] = A[idx[j]], A[idx[i]]             
        idx[i], idx[j] = idx[j], idx[i]
        ans += 1
        print(idx, A)
print(ans)
print(A)