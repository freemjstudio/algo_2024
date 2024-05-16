# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rorate_key(m):
    result = [[0] * m for _ in range(m)]  # key 를 담을 매트릭스
    for i in range(m):
        for j in range(m):
            result[j][m - i - 1] = result[i][j]

    return result


def check(new_lock):  # lock length

    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return False


def solution(key, lock):
    answer = True

    m, n = len(key), len(lock)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + m][j + m] = lock[i][j]

    for _ in range(4):  # rotation 방향
        key = rotate_key(key)  # new key
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock):
                    return True
                    # 되돌리기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False