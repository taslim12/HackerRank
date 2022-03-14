def count_substring(string, sub_string):
    i,j,k,count =0,0,0,0
    i =len(string)
    j = len(sub_string)
    while k+j <= i:
        if sub_string == string[ k : k+j ]:
            count = count + 1
        k = k + 1
    return count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)