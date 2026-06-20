# t 문자열의 모든 문자를 포함하는 s 문자열의 부분 문자열을 찾아서 리턴하라
# 만약 해당하는 부분 문자열이 없는 경우 빈 문자열을 리턴하라
# s, t의 길이는 1 ~ 50,000
class Solution:
    def count_char(self, string: str) -> str:
        count_dict = dict()
        for char in string:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        return count_dict

    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        answer = '#' * (m + 1)


        # 문자열의 순서는 상관 없으나, 중복을 고려하지 않고 개수는 일치해야 함
        # t의 각 문자열을 {A:1, B:1, C:1}로 카운트를 세 놓는다. -> O(N)
        t_count = self.count_char(t)

        left = 0
        window_t_count = dict.fromkeys(t_count.keys(), 0)
        matched_char_cnt = 0
        # 윈도우를 옮길 때 left를 빼거나 right을 더할텐데,
        # 이때 left나 right이 t에 있는 문자 중 하나라면,
            # 윈도우 안에서의 문자열 카운트 맵에서 해당 문자의 개수를 +- 1 하고
            # t_count[char] == window_t_count[char]이 같은지 비교한 후
            # 같다면 matched_char_cnt +- 1 한다.
            # matched_char_cnt == len(t_count)인 경우 answer를 업데이트한다.
        for right in range(m):
            cur_char = s[right]

            # t에 있는 문자인 경우
            if cur_char in t_count:
                window_t_count[cur_char] += 1 # window_t_count 업데이트
                if t_count[cur_char] == window_t_count[cur_char]: # 확장: 딱 충족되는 순간 +1
                    matched_char_cnt += 1
            
            # 조건이 충족되면 → 결과 후보를 기록하고 → left를 줄여서 더 짧은 윈도우를 시도
            while matched_char_cnt == len(t_count):
                substring = s[left:right + 1]
                if len(substring) < len(answer):
                    answer = substring

                prev_char = s[left]
                left += 1
                # t에 있는 문자인 경우
                if prev_char in t_count:
                    if t_count[prev_char] == window_t_count[prev_char]: # 수축: 딱 미충족으로 떨어지는 순간 -1
                        matched_char_cnt -= 1
                    window_t_count[prev_char] -= 1 # window_t_count 업데이트

            # 조건이 미충족이면 → right를 늘려서 더 많은 문자를 포함

        return '' if m < len(answer) else answer