
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []
    current_value=a1
    for i in range(0,n):
        AP_series.append(current_value)
        
        current_value=current_value+d
        print(AP_series[i], end=' ')
    print("\r")    
      

    # Complete this function to return A.P. series


    return AP_series


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the a1, d and n values
    for i in range(0,test_cases):
        a1,d,n=map(int,input().split())

        # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        AP_series = generate_AP(a1, d, n)

        # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series=list(map(lambda x: x**2, AP_series))
        for i in range(0,len(AP_series)):
    
             print(sqr_AP_series[i],end=' ') 
             
        print("\r")     

        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series = reduce((lambda x, y: x + y),sqr_AP_series)
        
    
        print(sum_sqr_AP_series) 
