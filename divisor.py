a=int(input("Enter the number:"))
result=[]
listr=range(1,a)
for i in listr:
    if a % i == 0:
     result.append(i)
print(result)