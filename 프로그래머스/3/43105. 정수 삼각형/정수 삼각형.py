def solution(tri):
    l = len(tri)
    tri.reverse()
    for i in range(l - 1):
        for j in range(l - i - 1):
            tri[i + 1][j] += max(tri[i][j], tri[i][j + 1])
    return tri[l - 1][0]