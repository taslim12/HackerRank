score_list,scores,final_list = [],[],[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        score_list.append([name,score])
    scores = sorted(set(scores))
    print('\n'.join(sorted([name for name,score in score_list if score == scores[1]])))
