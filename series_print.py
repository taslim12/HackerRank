from __future__ import print_function
from traceback import print_tb

if __name__ == '__main__':
    n = int(input("Enter a number"))

    x = range(1,n+1)
    if(n>=1 and n<=150):
        for y in x:
            print(y,end="")
