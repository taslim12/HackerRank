

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
if __name__ == '__main__':

    s = input()
    s= 'Taslim-haque'
    result = solve(s)
    print(result)