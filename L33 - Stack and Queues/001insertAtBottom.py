# time : (2n + 1).const ~ O(n)
# space: O(n) due to fn call stck
def insert_at_bottom(stk: list[int], val: int) -> None:
    # base case

    # if len(stk) == 0:
    #     stk.append(val)
    #     return

    if not stk:
        stk.append(val)
        return

    # recursive case

    top_val = stk.pop()
    insert_at_bottom(stk, val)
    stk.append(top_val)


stk = [10, 20, 30, 40, 50]
val = 0

print(stk)

insert_at_bottom(stk, val)

print(stk)  # [0, 10, 20, 30, 40, 50]
