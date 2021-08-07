x = 2
y = 3

# equality operators 
print(x == y)
z = x == y
print(z)
print(type(z))

print(x > y)
print(x < y)


print(x <= y)
print(x >= y)

pets = [1, 2, 3, "bob"]
print(1 in pets)
print("bob" in pets)
print(4 not in pets) # negation = not





if x == y:
    print("this is false")

if x <= y:
    print("this is true")

if x <= y:
    print("this is true")
else:
    print("this is false")

if x == y:
    print("this is true")
else:
    print("this is false")




if x == y and x < y:  # false and true = false, t and t = t, f and f = f
    print("this is true")
else:
    print("this is false")



if x == y or x < y:  # false or true = true, t or t = t, f or f = f    
    print("this is true")
else:
    print("this is false")


"""
truth table
P Q P^Q (^ = AND)
T F F
F T F
F F F
T T T

P Q P|Q (| = OR)
T F T
F T T 
T T T
F F F

P !P (! = NOT)
T F
F T
"""

if not x == y or not x < y:  # not - ang true mafalse, ang false matrue    
    print("this is true")
else:
    print("this is false")


if x == y:
    print("this is true")
elif not x < y:
    print("y is less than x")
else:
    print("this is false")


