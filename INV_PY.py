ta=int(input())
for t in range(ta):
    n=int(input())
    d=dict(input().split() for _ in range(n))
    o=int(input())
    for oa in range(o):
        op,item,num=input().split()
        num=int(num)
        #ol=ope[0]
        #oc=str(ol)
        #oa=oc.isupper()
        
        #ite1=ope[1]
        #num=int(ope[2])
        
        
        
    
        if item in d:
            
            if op=="ADD":
            
                d[item]=int(d[item])+num
                print("UPDATED Item "+item)
            if op=="DELETE":
                
                if int(d[item])<num:
                    print("Item "+item+" could not be DELETED")
                    
                else:
                    d[item]=int(d[item])-num
                    print("DELETED Item "+item)
        if item not in d.keys():
            if op=="ADD":
                d[item]=num
                print("ADDED Item "+item)
            if op=="DELETE":
                print("Item "+item+" does not exist ")
    di=dict((k,int(v)) for k,v in d.items())
    s=str(sum(di.values()))
    print("Total Items in Inventory: "+s)
    


