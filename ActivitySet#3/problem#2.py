from fractions import Fraction as f
n=int(input())
ll=[]
for i in range(n):
  f1=0
  m=int(input())
  l=input().split()
  for j in range(m):
      f1+=f(f'1/{l[j]}')
  ll.append(f1)
for i in ll:
  print(i)


  