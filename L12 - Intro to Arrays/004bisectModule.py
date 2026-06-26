# import bisect
import bisect as bi

# from bisect import *

arr = [10, 20, 30, 30, 30, 30, 30, 40, 50]
t = 30

print(bi.bisect_left(arr, t))
print(bi.bisect_right(arr, t))
print()

brr = [10, 20, 20, 30, 30, 30, 40, 40, 50]
t = 20
print(bi.bisect_left(brr, t))
print(bi.bisect_right(brr, t))
print()

crr = [100, 200, 300, 400, 500]
t = 350
print(bi.bisect_left(crr, t))
print(bi.bisect_right(crr, t))
print()

# bisect_left(arr, t) returns the 1st position or 1st index where the value is >= t
# bisect_right(arr, t) returns the 1st position or 1st index where the value is > t

drr = [1000, 2000, 300]
t = 50
print(bi.bisect_left(drr, t))
print(bi.bisect_right(drr, t))
print()

err = [100, 200, 300]
t = 500
print(bi.bisect_left(err, t))
print(bi.bisect_right(err, t))
