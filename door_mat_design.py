if __name__ == '__main__':
    # n, m = int(input()), int(input())
    list_input = input().split()
    n = int(list_input[0])
    m = int(list_input[1])
    initial_ = int((m-3)/2)
    text1 = '-'
    text2 = '.|.'
    text3 = 'WELCOME'
    i = 1
    initia2_ = 3
    for x in range(n):
        if(x < (n//2)):
            print((initial_*text1)+text2*i+(initial_*text1))
            initial_ = initial_ - 3
            i += 2
        if(x == (n//2)):
            print(text1*int((m-7)/2)+text3+text1*int((m-7)/2))
        if(x > (n//2)):
            print((initia2_*text1)+text2*(n-2)+(initia2_*text1))
            initia2_ = initia2_ + 3
            n -= 2