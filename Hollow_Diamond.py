n=int(input(''))
N=2*n
for i in range(0,N-1):
    for j in range(0,N-1):
        if i>=n:
            i=(N-2)%i
        if j<n:
            if i==n-j%n-1 :
                print('*',end='')
            else:
                print(' ',end='')
        else:
            if i==j%n+1:
                print('*',end='')
            else:
                print(' ',end='')
    print('')
