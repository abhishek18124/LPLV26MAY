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


# time : O(n^2)


def reverse_stack(stk: list[int]):
    # base case

    # if len(stk) == 0:
    #     return

    if not stk:
        return

    # recursive case

    top_val = stk.pop()
    reverse_stack(stk)
    insert_at_bottom(stk, top_val)


stk = [10, 20, 30, 40, 50]

print(stk)  # [10, 20, 30, 40, 50]

reverse_stack(stk)

print(stk)  # [50, 40, 30, 20, 10]
