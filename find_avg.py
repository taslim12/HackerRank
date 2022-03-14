
avg = 0.0
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    
    query_name = input()
    for key in student_marks:
        if key == query_name:
            avg = sum(list(student_marks[key]))/3
    avg = "{:.2f}".format(avg)
    print(avg)
            