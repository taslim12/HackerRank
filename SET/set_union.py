n = int(input())
english = set(map(int, input().split()))
n2 = int(input())
french = set(map(int, input().split()))

list = []
list = english.union(french)
print(len(list))