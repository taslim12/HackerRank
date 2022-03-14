if __name__ == '__main__':
    N = int(input())
    p_list = []
    for x in range(0,N):
        list_input = input().split()
        if list_input[0] == 'append':
            p_list.append(int(list_input[1]))
            print(p_list)
        elif list_input[0] == 'insert':
            p_list.insert(int(list_input[1]),int(list_input[2]))
            print(p_list)
        elif list_input[0] == 'print':
            print(p_list)
            print(p_list)
        elif list_input[0] == 'remove':
            p_list.remove(list_input[1])
            print(p_list)
        elif list_input[0] == 'sort':
            p_list.sort()  
            print(p_list)
        elif list_input[0] == 'pop':
            p_list = p_list[:-1]
            print(p_list)
        elif list_input[0] == 'reverse':
            p_list.reverse()
            print(p_list)
