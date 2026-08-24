from collections import Counter

s = input()
n = len(s)

t = input()
k = len(t)

t_freq_map = Counter(t)

print(t_freq_map)

win_freq_map = Counter()

i = 0  # represents start of the window
j = 0  # represents end of the window

# window extends from [i, j)

# 1. build the freq_map for the 1st window

while j < k:
    win_freq_map[s[j]] += 1
    j += 1

print(win_freq_map)

ans = 0

if win_freq_map == t_freq_map:
    ans += 1

# 2. build the freq_map for the remaining windows

while j < n:
    # slide the window

    win_freq_map[s[i]] -= 1
    # if win_freq_map[s[i]] == 0:
    #     del win_freq_map[s[i]]
    i += 1
    win_freq_map[s[j]] += 1
    j += 1

    print(win_freq_map)

    # update the ans
    if win_freq_map == t_freq_map:
        ans += 1


print(ans)
