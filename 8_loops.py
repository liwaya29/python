for i in range(1,11):
    print(i)
print()
print()
x = ["a", "b", "c", "d", "e"]
for e in x:
    print(e)

for i in range(1,11):
    print(i + 1)

x = ["a", "b", "c", "d", "e"]
for e in x:
    print("this is letter " + e)


a = "a"
b = "b"
a += b # compound operator
# a = a + b
print(a)



"""
*
**
***
****
*****
"""
print()
print()
for v in range(1,6):
    print("*" * v )

"""
v = 1; *
v = 2; **
v = 3; ***
v = 4; ****
v = 5; *****
"""



"""
*****
****
***
**
*
"""
print()
print()
m = 6
for v in range(1,m):
    print("*" * ( m - v))
    


"""
1 odd
2 even
3 odd
"""
print()
print()
for i in range(1,11):
    w = str(i)
    if i%2==0:
        w += " even"
    else:
        w += " odd"
    print(w)



"""
    *
   **
  ***
 ****
*****
"""
print()
print()
m = 6
for v in range(1,m):
#    print("_" * (m - v - 1) "*" * v)
    print("%s%s" % (" " * (m - v - 1),"*" * v))



"""
*
**
***
****
*****
****
***
**
*
"""
print()
print()
m = 10
c = m/2
for v in range(1,m):
    if v<=c:
        print("*" * v)
    else:
        print("*" * (m - v))



"""
*****
****
***
**
*
**
***
****
*****
"""
print()
print()
m = 10
c = m/2
for v in range(1,m):
    if v<=c:
        print("*" * (m - v - 4))
    else:
        print("*" * (v-4))
