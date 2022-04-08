def draw_star(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            if j%5==0 :
                print("#", end=' ')
            else:
                print("*",end=' ')
        print("\r")
T=int(input())
for k in (0,T):
    n = int(input())
    draw_star(n)
    