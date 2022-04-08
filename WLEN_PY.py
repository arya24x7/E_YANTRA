T=int(input())
for i in range(0,T):
    x=input().split()
    
    for i in range(0,len(x)):
        if i!=len(x)-1:
            print(len(x[i]),end=',')
        else :
            print(len(x[i]))


