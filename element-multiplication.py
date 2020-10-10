l=[int(x) for x in input().split(",")]
l2=[]
l3=[]
result=1
for x in l:
    result = result * x  
l2.append(result)
for i in range(len(l)):
    for x in l2:
        l3.append(x)
l3
res = [j // i for i, j in zip(l, l3)] 
res
