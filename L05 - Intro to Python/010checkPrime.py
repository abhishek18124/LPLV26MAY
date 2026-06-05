n = int(input())

i = 2

while i * i <= n:
    if n % i == 0:
        print("not prime")
        break
    i = i + 1
else:
    print("prime")

"""
while can have an else clause which
runs when you terminate the loop 
normally, in case you break then 
else is not executed
"""
