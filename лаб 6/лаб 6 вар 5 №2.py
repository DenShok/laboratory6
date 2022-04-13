lst = [1,3,5,6,4,7,9,4,8,3,4,6]

for i in reversed(range(len(lst)-1)):

   if lst[i] in lst[i+1:]:

       lst.pop(i)

print(lst)
