
T=int(input())
array=[]

for i in range(0,T):
    L=int(input())
    array=input().split()
    rev=array[::-1]
    for i in range(0,L):
        print(rev[i],end=' ')
    print("\r")    
    for i in range(1,L):
        if i%3==0:
            array[i]=int(array[i])
            Aarray=array[i]+3
            print(Aarray,end=' ')
    print("\r")        
    for i in range(1,L):        
        if i%5==0:
            array[i]=int(array[i])
            Aarray=array[i]-7
            print(Aarray,end=' ')
    print("\r")    
    sum_array=array[3:8]
    sum_int=[]
    for i in range(0,len(sum_array)):
        x=int(sum_array[i])
        sum_int.append(x)
        
        
    def _sum(arr): 
    
        sum=0
      
    
        for i in range(0,len(arr)):
            sum = sum + arr[i]
          
        return(sum)
    sum_ans=_sum(sum_int)  
    print(sum_ans)
    
    
             
            
            
    

