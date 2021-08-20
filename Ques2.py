a=int(input())
d=[]
for i in range(a):
  b=input()
  c=b.split()
  a1=int(c[0])
  a2=int(c[1])
  trips=a1
  while a1>=a2:
    trips+=(a1//a2)
    a1=a1//a2+a1%a2
  d.append(trips)

for j in d:
  print(str(j))
  
  # correct code
