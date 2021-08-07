"""
1
2
3 fizz
4
5 buzz
6 fizz
.
9 fizz
10 buzz
.
12 fizz
.
15 fizz buzz
.
100
"""

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i, "fizz buzz")
    elif i%3==0:
        print(i, "fizz")
    elif i%5==0:
        print(i, "buzz")
    else:
        print(i)
"""
i = 1; 1
i = 2; 2
i = 3; 3
       3 fizz
.  
.
i = 15; 15
        15 fizz
        15 buzz
"""


