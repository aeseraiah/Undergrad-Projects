#i needs to be defined
i = 0

while i < 3:
    print("hello")
    i += 1


#x does not need to be defined, for loops starts at 0
x = 1
for x in range(3): 
    print(x)


print("new_hello\n" * 3, end="")

def main():
    num = get_number()
    func()

def get_number():
    #inducing infinite loop
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def func(n):
    for i in range(n):
        print("newer_hello")

def main():
    num = get_number()
    func(num)

main()



