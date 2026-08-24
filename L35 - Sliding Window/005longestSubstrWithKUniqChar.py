from collections import defaultdict

s = input()
n = len(s)
k = int(input())


i = 0  # represents start of the window
j = 0  # represents end of the window

# window extends from [i, j)

win_freq_map = defaultdict(int)
max_so_far = 0
win_uniq_cnt = 0

while j < n:
    # expand the window

    win_freq_map[s[j]] += 1
    if win_freq_map[s[j]] == 1:
        win_uniq_cnt += 1

    j += 1

    # check for violation of window property

    while win_uniq_cnt > k:
        win_freq_map[s[i]] -= 1
        if win_freq_map[s[i]] == 0:
            win_uniq_cnt -= 1
            del win_freq_map[s[i]]

        i += 1

    # check if the current window is valid
    if win_uniq_cnt == k:
        max_so_far = max(max_so_far, j - i)


print(max_so_far)

# time : O(n)
# space: 26 due to freq_map assuming input string contains a-z ~ const i.e. O(1)
