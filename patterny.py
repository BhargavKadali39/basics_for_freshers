x = 0
n = 5
for i in range(0,n):
    x+=1
    for j in range(0,i+1):
        print(x,end="")
    print("\r")
