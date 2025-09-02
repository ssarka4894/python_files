import numpy as np

def display_pattern(num):
    for i in range(num):
        a = ""
        for j in range(num):
            if (i <= j):
                a = a + "*"
            else:
                a = a + " "
        print(a)
if __name__ == '__main__':
    print("Here is the pattern!")
    display_pattern(10)
