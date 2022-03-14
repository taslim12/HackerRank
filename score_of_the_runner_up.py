if __name__ == '__main__':
    n = int(input())
    arr= map(int, input().split())


    arr=sorted(arr)
    p = -1
    for x in arr:
        if(arr[p] > arr[p-1]):
            print(arr[p-1])
            break
        else:
            p = p -1

 