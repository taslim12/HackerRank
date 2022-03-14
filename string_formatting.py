def print_formatted(number):
    substring = ''
    split_string = []
    lenth = len(bin(number)[2:])
    for n in range(1,number+1):
        substring = oct(n)[1:]
        print(str(n).rjust(lenth)+ ' '+ substring.rjust(lenth)+' '+ 
        str(hex(n)[2:].rjust(lenth)).upper() + ' ' +bin(n)[2:].rjust(lenth))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)