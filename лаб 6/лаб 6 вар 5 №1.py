lst = [1,2,2,3,3,5,5,2,1,1]
for i in range(len(lst)-1):
    print(lst[i],lst[i+1]) if lst[i] == lst[i+1] and lst[i]%2>0 else None
