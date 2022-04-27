divisible_by_7=[]
for numb in range(100,200):
 if(numb%7==0):
  divisible_by_7.append(numb)
print(divisible_by_7)


x = ['a','b','a','e','d','b','c','e','f','g','h']
x2=list(set(x))
print(x2)

smallest=[3,6,8,2,4,1,5,7]
small=min([3,6,8,2,4,1,5,7])
print(small)

x = [[1,2],[3,4],[5,6]]
mo=x[0]+x[1]+x[2]
print(mo)


num = int (input ("Enter the number:"))
if num%3 == 0:
              print ("The number is divisible.")
else:
              print ("The number is not divisible.")
              
              x = [100,110,120,130,140,150]
m=[m*5 for m in x ]
print(m)           