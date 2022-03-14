# Enter your code here. Read input from STDIN. Print output to STDOUT
def average(m,m_arr,n,n_arr):
    set_1 = set(m_arr)
    set_2 = set(n_arr)
    set_1.symmetric_difference_update(set_2)
    for x in sorted(list(set_1)):
        print(x)

if __name__ == '__main__':
    m = int(input())
    m_arr = list(map(int, input().split()))
    n = int(input())
    n_arr = list(map(int, input().split()))
    if(len(m_arr) == m and len(n_arr) == n):
        average(m,m_arr,n,n_arr)
    else:
        print("Error")