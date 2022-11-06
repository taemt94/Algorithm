def solution(survey, choices):
    score_map = {'R': 0, 'T': 0,
                 'C': 0, 'F': 0,
                 'J': 0, 'M': 0,
                 'A': 0, 'N': 0}
    survey_list = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for s, c in zip(survey, choices):
        if c < 4:
            score_map[s[0]] += 4 - c
        elif c > 4:
            score_map[s[1]] += c - 4
    
    answer = ''
    for sur in survey_list:
        if score_map[sur[0]] >= score_map[sur[1]]:
            answer += sur[0]
        else:
            answer += sur[1]    
    return answer