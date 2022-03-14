n = int(input())
s = set(map(int, input().split()))
n2 = int(input())
commands = []

for x in range(n2):
    command = input().split()
    commands.append(command)

for x in commands:
    if x[0] == 'pop' and len(s) >= 1:
        s.pop()
        print(s)
    elif x[0] == 'remove' and len(x) > 1:
        if(int(x[1]) in s):
            s.remove(int(x[1]))
            print(s)
    elif x[0] == 'discard':
        s.discard(int(x[1]))
        print(s)

print(sum(s))


