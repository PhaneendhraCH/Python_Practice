def outer():   

    print("outer function started")   

    def inner():   
        print("inner function execution")   

    print("outer function returning inner function")   
    return inner   

f1 = outer() # this returns innner function..
f1() # everytime you call f1.. inner function will be executed..
f1()
f1()

#-------------------------------------------------------------------------#
# Patterns

"""

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * *

"""
print("\nPattern - 1\n")
for i in range(1,8):
    print(f"{'*'*i}")


"""

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9 
10 10 10 10 10 10 10 10 10 10

"""
print("\nPattern - 2\n")
for i in range(1,11):
    char = str(i) + " "
    print(f"{char*i}")



"""

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8 9 
1 2 3 4 5 6 7 8 9 10 
"""
print("\nPattern - 3\n")
for i in range(1,11):
    for n in range(1,i+1):
        print(f"{n}",end=" ")
    print()


"""

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8 9 
1 2 3 4 5 6 7 8 9 10 
"""
print("\nPattern - 4\n")
for i in range(1,11):
    for n in range(1,i+1):
        print(f"{n}",end=" ")
    print()

"""

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
1 0 1 0 1 0 1 

"""
print("\nPattern - 5\n")
start = "1"
for i in range(1,8):
    if i == 1:
        print(start)
    else:
        start = ("0" if start[0] == "1" else "1") + " " + start
        print(start)


"""

 5 5 5 5 5 
  4 4 4 4 
   3 3 3 
    2 2 
     1 

"""
print("\nPattern - 6\n")
for i in range(5,0,-1):
    print(" "*(6-i),end="")
    char = str(i) + " "
    print(f"{char * i}")


"""

* * * * * 
  * * * * 
   * * * 
    * * 
     * 

"""
print("\nPattern - 7\n")
for i in range(5,0,-1):
    print(" "*(6-i),end="")
    char = "*" + " "
    print(f"{char * i}")

"""

A B C D E 
  A B C D 
    A B C 
      A B 
        A

"""

print("\nPattern - 9\n")
start = 65
for i in range(5,0,-1):
    print("  "*(5-i),end="")
    for i in range(0,i):
        char = str(chr(65+i)) + " "
        print(char,end="")
    print()