n=int(input())
num=n+n
for i in range(0,num):
    for j in range(0,num):
        if((i+j)==(num-1)):
            print("*",end="")
        elif(i==j):
            print("*",end="")
        else:
            print(".",end="")
    print()
