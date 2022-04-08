T=int(input())
for i in range(0,T):
    n=int(input())
    x=[]
    y=[]
    
    for i in range(0,n):
        p,q=input().split()
        q=float(q)
        x.append(p)
        y.append(q)
    print(y)    
    max_score=max(y)
    for i in range(0,n):
        if y[i]==max_score:
            high_scorer=x[i]
            print(high_scorer)
        
    