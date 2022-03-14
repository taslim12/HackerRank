if __name__ == '__main__':
    s = input()
    result_1 = result_2 = result_3 = result_4 = result_5 = 'False'

    for x in s:
        if str.isalnum(x) == True:
            result_1 = 'True'
        if str.isalpha(x) == True:
            result_2 = 'True'
        if str.isdigit(x) == True:
            result_3 = 'True'
        if str.islower(x) == True:
            result_4 = 'True'
        if str.isupper(x) == True:
            result_5 = 'True'
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)