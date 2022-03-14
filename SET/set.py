def average(array):
    # your code goes here
    set_array= set(array)
    length = len(set_array)
    avg =  sum(list(set_array))/length
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)