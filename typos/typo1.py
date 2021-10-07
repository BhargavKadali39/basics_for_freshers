n = 5
for x, i in enumerate(range(n), start=1):
    for _ in range(i+1):
        print(x,end="")
    print("\n")
