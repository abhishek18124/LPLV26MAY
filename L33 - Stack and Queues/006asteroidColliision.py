class Solution:
    # time : O(n)
    # space: O(n) due to stack
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            if ast < 0 and stk and stk[-1] > 0:
                # collisions will happen
                flag = True  # assume ast will survive collisions
                while stk and stk[-1] > 0:
                    if abs(ast) > stk[-1]:
                        stk.pop()
                    elif abs(ast) < stk[-1]:
                        flag = False
                        break
                    else:
                        # abs(ast) == stk[-1]
                        stk.pop()
                        flag = False
                        break
                if flag:
                    # ast has survived all the collisions so track it
                    stk.append(ast)
            else:
                stk.append(ast)

        return stk
