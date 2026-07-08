from collections import defaultdict

# time : n (to build f1) + n (to build f2) + 26 (to compare f1 and f2)
# space: 26 for f1 + 26 for f2 ~ O(1)


def is_anagram(s1: str, s2: str) -> bool:
    f1 = defaultdict(int)
    for ch in s1:
        f1[ch] += 1

    # print(f1)

    f2 = defaultdict(int)
    for ch in s2:
        f2[ch] += 1

    # print(f2)

    return f1 == f2


s1 = input()
s2 = input()

print("anagram") if is_anagram(s1, s2) else print("not an anagram")
