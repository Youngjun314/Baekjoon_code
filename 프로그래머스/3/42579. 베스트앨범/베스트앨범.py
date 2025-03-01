def solution(genres, plays):
    d = dict()
    answer = list()
    for i, j in enumerate(genres):
        if j in d.keys():
            d[j][0] += plays[i]
            d[j].append(i)
        else:
            d[j] = [plays[i], i]
    return sorted(d.values(), reverse = True)
