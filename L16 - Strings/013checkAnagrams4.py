# time : n (to build f1) + n (to build f2) + 26 (to compare f1 and f2)
# space: 26 for f1 + 26 for f2 ~ O(1)


def is_anagram(s1: str, s2: str) -> bool:
    f1 = [0] * 26
    for ch in s1:
        idx = ord(ch) - ord("a")
        f1[idx] += 1

    print(f1)

    f2 = [0] * 26
    for ch in s2:
        f2[ord(ch) - ord("a")] += 1

    print(f2)

    return f1 == f2


s1 = input()
s2 = input()

print("anagram") if is_anagram(s1, s2) else print("not an anagram")
