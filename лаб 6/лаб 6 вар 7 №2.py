mas= [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]

minim=min(mas)

maxim=max(mas)

i_minim=0

i_maxim=0

for i in range(len(mas)):

   if mas[i]==minim:

       i_minim=i

   if mas[i]==maxim:

       i_maxim=i

mas[i_minim]=maxim

mas[i_maxim]=minim
