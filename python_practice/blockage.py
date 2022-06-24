def main():
    #print_row(4)
    #print_column(3)
    #print_square(3)
    better_print_square(3)

def print_column(height):
    for x in range(height):
        print("#")

def print_row(width):
    print("#" * width)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        print()

#OR, more abstractly using our functions..

def better_print_square(size):
    for i in range(size):
        print_row(size)

main()



