import sys

T = int(sys.stdin.readline())

freshmen_cnt_list = []
for _ in range(T):
    N = int(sys.stdin.readline())
    scores = []
    for _ in range(N):
        score = list(map(int, sys.stdin.readline().split()))
        scores.append(score)
    scores.sort(key= lambda x: x[0])
    
    freshmen_cnt = 1
    score_base = scores[0][1]
    for score in scores[1:]:
        if score[1] < score_base:
            freshmen_cnt += 1
            score_base = score[1]
    freshmen_cnt_list.append(freshmen_cnt)
[print(cnt) for cnt in freshmen_cnt_list]