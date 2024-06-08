def solution(s):
    idx = int(len(s) / 2)
    return s[idx] if len(s) % 2 != 0 else s[slice(idx - 1, idx + 1)]
    