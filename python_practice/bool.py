def main():
    x = int(input("What's x? "))
    if is_even_best(x):
        print("Even")
    else:
        print("odd")
    


def is_even(b):
    if b % 2 == 0:
        return True
    else:
        return False

def is_even_better(b):
    return True if b % 2 == 0 else False

def is_even_best(b):
    # == uses boolean logic and therefore returns True/False
    return b & 2 == 0




main()