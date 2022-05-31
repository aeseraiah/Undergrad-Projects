x = input("What's an int value of x? ")
y = input("What's an int value of y? ")

z = x + y

#z prints the concatenation of x + y since they are considered strings. 
print(z)

print(int(x) + int(y))

#a+b prints the concatenation 

a = int(input("What's a? "))
b = int(input("What's b? "))

print(a + b)


d = float(input("What's d? "))
e = float(input("What's e? "))

print(d+e)

f = round(d + e, 2)
print(f)

#if you want to format your rounded number to include the command in a bigger integer:
print(f"{f:,}")
#OR if you want to round JUST using python's formatting:
print(f"{f:.2f}")
