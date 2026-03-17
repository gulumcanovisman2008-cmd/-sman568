ls = []

with open('adamlar.csv','r') as a:
  L = list(a)
  for i in range(1,len(L)-1):
    ls.append(L[i].split(',')[2].strip('\n'))

ls = sorted(ls,reverse=True)

print(ls)
  

