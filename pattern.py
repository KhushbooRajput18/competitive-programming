#n=int(input("Enter a number:"))
#for i in range(0,n):
 #   print("*",end="")


#n=int(input("enter a number"))
#m=int(input("enter a number"))
#for i in range(0,n):
 #   for j in range (0,m):
  #      print("*",end="")
#print()  ;

n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()    

n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()    


