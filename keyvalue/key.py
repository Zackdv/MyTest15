n=int(input('Enter Number:'))
if n==1:
    print('This is Not a Prime Number')

if n>1:
    for x in range(2,n):
        if n%x==0:
            print('This is Not a Prime Number')
            break
    else:
        print('Its a Prime Number',)



















































































