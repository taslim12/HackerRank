def print_rangoli(n):
    number = n
    x,alphabets,final='','',[]
    for i in range(number):
        alphabets+=chr(97+i)

    for i in alphabets[::-1]:
        x+="-"+i
        final.append(x+x[:-1][::-1])
        final[-1]=final[-1].strip('-')
    for i in final:
        print(i.center(len(final[-1]),'-'))

    for i in final[::-1][1:]:
        print(i.center(len(final[-1]),'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)