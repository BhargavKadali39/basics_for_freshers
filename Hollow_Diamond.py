n=int(input(''))
N=2*n
for i in range(N-1):
    for j in range(N-1):
        if i>=n:
            i=(N-2)%i
        if j<n:
            if i==n-j%n-1 :
                print('*',end='')
            else:
                print(' ',end='')
        elif i==j%n+1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
