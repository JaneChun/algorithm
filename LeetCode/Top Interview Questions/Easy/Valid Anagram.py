# 두 문자열 s와 t가 주어졌을 때, t가 s의 애너그램(anagram) 이면 true를 반환하고, 그렇지 않으면 false를 반환하세요.
# 애너그램이란, 한 문자열의 문자들을 재배열해서 다른 문자열을 만들 수 있는 경우를 말합니다.

# 1 <= s.length, t.length <= 5 * 10^4
# s와 t는 소문자 영어 알파벳으로만 이루어져 있습니다.

import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()


def count_char(str):
    count_dict = {}

    for i in range(len(str)):
        char = str[i]

        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    return count_dict


def check_anagram(s, t):
    flag = True

    for i in range(len(s)):
        s_char, s_count = s[i]
        t_char, t_count = t[i]

        if s_char == t_char and s_count == t_count:
            continue
        else:
            flag = False
            break

    return flag


s_dict = count_char(s)
t_dict = count_char(t)

sorted_s_list = list(sorted(s_dict.items()))
sorted_t_list = list(sorted(t_dict.items()))

if len(sorted_s_list) != len(sorted_t_list):
    print(False)
else:
    result = check_anagram(sorted_s_list, sorted_t_list)
    print(result)
