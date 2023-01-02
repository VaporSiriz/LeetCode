
def isSubsequence(s: str, t: str) -> bool:
    # location_s_alpha = {}
    # for alpha_s in s:
    #     location_s_alpha[alpha_s] = -1
    #     for index, alpha_t in enumerate(t):
    #         if alpha_s == alpha_t:
    #             location_s_alpha[alpha_s] = index
    #             break
    #     if location_s_alpha[alpha_s] == -1:
    #         return False

    # arrangement_s = []
    # for alpha_s in s:
    #     arrangement_s.append(location_s_alpha[alpha_s])
    # for index in range(1, len(arrangement_s)):
    #     if arrangement_s[index] < arrangement_s[index-1]:
    #         return False

    # return True
    # # 같은 문자도 나올 수 있다. => Wrong Code

    # 새로운 풀이
    # string t의 처음부터 string s의 element를 탐색해가는데,
    # 만약 s의 element가 존재한다면 다음 element를 탐색.
    # 예상, 최상의 경우 O(len(s)), 최악의 경우 O(len(t))
    index_s = 0
    len_s = len(s)
    len_t = len(t)
    for index_t, alpha_t in enumerate(t):
        # string s의 element가 
        print(f"{alpha_t} - {s[index_s]}")
        if alpha_t == s[index_s]:
            index_s += 1
        # t의 남은 길이가 s의 남은 길이보다 작을 때 False
        if len_t - index_t < len_s - index_s:
            return False
    print(f"{index_s} ?= {len_s-1}")
    return index_s == len_s

print(isSubsequence("abc", "ahbgdc"))