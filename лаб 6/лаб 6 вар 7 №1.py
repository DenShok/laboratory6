mas= [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]

sum_chetn=0

proizved=1

for i in range(len(mas)):

   if mas[i]%2!=0:

       proizved*=mas[i]

   else:

       sum_chetn+=mas[i]

print("Сумма:", sum_chetn)

print("Произведение:", proizved)
