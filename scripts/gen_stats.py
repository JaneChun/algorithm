#!/usr/bin/env python3
"""
푼 문제 통계를 집계해서 README.md의 마커 구간(STATS:START ~ STATS:END)만 교체한다.
마커 밖(헤더 등 수동 작성분)은 건드리지 않는다.

문제 1개의 정의(사이트별 상이):
  - 백준           : 백준/{티어}/{문제}/...          → 문제 = 폴더
  - 프로그래머스   : 프로그래머스/{레벨}/{문제}/...   → 문제 = 폴더 (레벨 이름 원본 유지)
  - LeetCode       : Problems/{문제}/  +  Top Interview Questions/{난이도}/{파일}
  - HackerRank     : HackerRank/{파일}               → 문제 = 파일

LeetCode 난이도:
  - Problems/*/README.md 의 'Difficulty-<Easy|Medium|Hard>' 배지에서 파싱 (크롬 익스텐션 커밋)
  - Top Interview Questions/* 는 난이도 정보가 없어 아래 TOP_INTERVIEW_DIFFICULTY 로 고정 매핑
    (앞으로는 익스텐션으로만 커밋 → Problems 로만 늘어나므로 이 표는 갱신 불필요)
"""
import collections
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
IGNORE_TOP = {".git", ".github", "scripts", ".vscode", "node_modules"}
START, END = "<!-- STATS:START -->", "<!-- STATS:END -->"

TIER_ORDER = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"]
LEVEL_ORDER = ["Lv0", "Lv1", "Lv2", "Lv3", "Unrated"]

# 수동 커밋된 Top Interview Questions 문제들의 난이도 (파일명 기준)
TOP_INTERVIEW_DIFFICULTY = {
    "Best Time to Buy and Sell Stock II": "Medium",
    "Binary Tree Level Order Traversal": "Medium",
    "Contains Duplicate": "Easy",
    "Delete Node in a Linked List": "Medium",
    "First Unique Character in a String": "Easy",
    "Maximum Depth of Binary Tree": "Easy",
    "Merge Sorted Array": "Easy",
    "Merge Two Sorted Lists": "Easy",
    "Remove Duplicates from Sorted Array": "Easy",
    "Remove Nth Node From End of List": "Medium",
    "Reverse Integer": "Medium",
    "Reverse Linked List": "Easy",
    "Reverse String": "Easy",
    "Rotate Array": "Medium",
    "Symmetric Tree": "Easy",
    "Valid Anagram": "Easy",
    "Validate Binary Search Tree": "Medium",
}

# solved.ac 티어 아이콘 번호 (Bronze=1~5 → 대표값, Silver=6~10, Gold=11~15)
TIER_ICON = {"Bronze": 3, "Silver": 8, "Gold": 13, "Platinum": 18, "Diamond": 23, "Ruby": 28}


# ----------------------------------------------------------------------------- 파일 수집
def rel_paths():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_TOP and not d.startswith(".")]
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT)
            if not rel.startswith("."):
                yield rel.replace(os.sep, "/")


def problem_key(rel):
    p = rel.split("/")
    site, last = p[0], p[-1].lower()
    if site == "백준" and len(p) >= 3:
        return ("백준", p[1], p[2])
    if site == "프로그래머스" and len(p) >= 3:
        return ("프로그래머스", p[1], p[2])
    if site == "LeetCode" and len(p) >= 3 and p[1] == "Problems":
        return ("LeetCode", "Problems", p[2])
    if site == "LeetCode" and len(p) >= 4 and p[1] == "Top Interview Questions" and last != "readme.md":
        return ("LeetCode", "TopInterview", p[3])
    if site == "HackerRank" and len(p) >= 2 and last != "readme.md":
        return ("HackerRank", p[-1])
    return None


def norm_level(level):
    key = level.lower().replace("lv.", "").replace("lv", "").strip()
    table = {"0": "Lv0", "1": "Lv1", "2": "Lv2", "3": "Lv3"}
    if key in table:
        return table[key]
    if level.lower() == "unrated":
        return "Unrated"
    return level


# ----------------------------------------------------------------------------- 집계
problems = {k for k in (problem_key(r) for r in rel_paths()) if k}

site_totals = collections.Counter()
baekjoon = collections.Counter()
programmers = collections.Counter()
for key in problems:
    site_totals[key[0]] += 1
    if key[0] == "백준":
        baekjoon[key[1]] += 1
    elif key[0] == "프로그래머스":
        programmers[norm_level(key[1])] += 1

# LeetCode 난이도: Problems 는 README 파싱, Top Interview 는 고정 매핑
leetcode = collections.Counter()
problems_dir = os.path.join(ROOT, "LeetCode", "Problems")
if os.path.isdir(problems_dir):
    for slug in os.listdir(problems_dir):
        readme = os.path.join(problems_dir, slug, "README.md")
        if os.path.isfile(readme):
            with open(readme, encoding="utf-8") as fh:
                m = re.search(r"Difficulty-(Easy|Medium|Hard)", fh.read())
            leetcode[m.group(1) if m else "Unknown"] += 1

top_dir = os.path.join(ROOT, "LeetCode", "Top Interview Questions")
if os.path.isdir(top_dir):
    for cur, _dirs, files in os.walk(top_dir):
        for name in files:
            if name.lower() == "readme.md":
                continue
            stem = os.path.splitext(name)[0]
            leetcode[TOP_INTERVIEW_DIFFICULTY.get(stem, "Unknown")] += 1

total = sum(site_totals.values())


# ----------------------------------------------------------------------------- 렌더 헬퍼
def sh(label, color, extra=""):
    return f"https://img.shields.io/badge/{label}-{color}?style=flat-square{extra}"


LV_BADGE = {
    "Lv0": f"![Lv0]({sh('Lv0', 'CFE8FA', '&logoColor=black')})",
    "Lv1": f"![Lv1]({sh('Lv1', '90CAF9', '&logoColor=black')})",
    "Lv2": f"![Lv2]({sh('Lv2', '42A5F5')})",
    "Lv3": f"![Lv3]({sh('Lv3', '1565C0')})",
    "Unrated": f"![Unrated]({sh('Unrated', '9E9E9E')})",
}
HR_BADGE = f"![Unrated]({sh('Unrated', '9E9E9E')})"
DIFF_BADGE = {
    "Easy": f"![Easy]({sh('Easy', '00B8A3')})",
    "Medium": f"![Medium]({sh('Medium', 'FFC01E')})",
    "Hard": f"![Hard]({sh('Hard', 'FF375F')})",
}
JS_BADGE = f"![JS]({sh('', 'F7DF1E', '&logo=javascript&logoColor=black')})"
PY_BADGE = f"![Py]({sh('', '3776AB', '&logo=python&logoColor=white')})"


def tier_img(tier):
    return f'<img src="https://static.solved.ac/tier_small/{TIER_ICON[tier]}.svg" width="16">'


def cell(pairs):
    """[(badge, count), ...] → 'badge N<br>badge N' 형태의 표 셀."""
    return "<br>".join(f"{badge} {count}" for badge, count in pairs if count)


# ----------------------------------------------------------------------------- 셀 구성
prog_cell = cell([(LV_BADGE[k], programmers.get(k, 0)) for k in LEVEL_ORDER])
baek_cell = cell([(tier_img(k), baekjoon.get(k, 0)) for k in TIER_ORDER])
lc_cell = cell([(DIFF_BADGE[k], leetcode.get(k, 0)) for k in ["Easy", "Medium", "Hard"]])

pg = site_totals["프로그래머스"]
bj = site_totals["백준"]
lc = site_totals["LeetCode"]
hr = site_totals["HackerRank"]
hr_cell = f"{HR_BADGE} {hr}"

block = f"""{START}
<div align="center">

### 🧩 TOTAL SOLVED: {total} 문제

<br />

| 플랫폼 | 문제 수 | 난이도별 문제 수 | 기간 |
|:---|:---:|:---|:---|
| 프로그래머스 | {pg} | {prog_cell} | 2022.11 ~ 2024.04 {JS_BADGE} <br> 2024.04 ~ 2026.01 {PY_BADGE} |
| 백준 | {bj} | {baek_cell} | 2026.01 ~ 2026.05 |
| LeetCode | {lc} | {lc_cell} | 2026.05 ~ 현재 |
| HackerRank | {hr} | {hr_cell} |

</div>
{END}"""


# ----------------------------------------------------------------------------- README 주입
with open(README, encoding="utf-8") as fh:
    content = fh.read()

if START in content and END in content:
    content = re.sub(re.escape(START) + ".*?" + re.escape(END),
                     lambda _: block, content, flags=re.S)
else:
    content = content.rstrip() + "\n\n" + block + "\n"

with open(README, "w", encoding="utf-8") as fh:
    fh.write(content)

unknown = leetcode.get("Unknown", 0)
print(f"총 {total}문제 · 프로그래머스 {pg} · 백준 {bj} · LeetCode {lc} · HackerRank {hr}")
print(f"프로그래머스: " + " ".join(f"{k}{programmers.get(k,0)}" for k in LEVEL_ORDER))
print(f"백준:       " + " ".join(f"{k}{baekjoon.get(k,0)}" for k in TIER_ORDER if baekjoon.get(k)))
print(f"LeetCode:   Easy{leetcode['Easy']} Medium{leetcode['Medium']} Hard{leetcode['Hard']}"
      + (f"  ⚠️ Unknown{unknown}" if unknown else ""))
