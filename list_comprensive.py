from __future__ import print_function
from traceback import print_tb

if __name__ == '__main__':
    x = int(input("Enter a number"))
    y = int(input("Enter a number"))
    z = int(input("Enter a number"))
    n = int(input("Enter a number"))

    x_list = [p for p in range(0,x+1)]
    y_list = [p for p in range(0,y+1)]
    z_list = [p for p in range(0,z+1)]
    final_list_2 = [(x,y,z) for x in x_list for y in y_list for z in z_list if x+y+z != n]
    print(final_list_2)