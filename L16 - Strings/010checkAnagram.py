# time : nlogn + nlogn + n ~ O(nlogn)
# space: n + n ~ O(n)


def is_anagram(s1: str, s2: str) -> bool:
    sorted_s1 = "".join(sorted(s1))
    print(sorted_s1)
    sorted_s2 = "".join(sorted(s2))
    print(sorted_s2)
    return sorted_s1 == sorted_s2


s1 = input()
s2 = input()

print("anagram") if is_anagram(s1, s2) else print("not an anagram")
