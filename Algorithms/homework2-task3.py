# Даны 2 последовательности pushed и popped, содержащие уникальные целые числа. popped  является перестановкой pushed, то есть, все элементы совпадают, но может отличаться порядок.

# Программа должна вернуть True, если эти последовательности могут получиться в результате некоторой последовательности операций push и pop на пустом стеке.

# 1 <= len(pushed) <= 100_000

 

# Пример 1:

# pushed: 1 2 3 4 5

# popped: 1 3 5 4 2

# result: True

# Последовательность операций: push(1), pop(1), push(2), push(3), pop(3), push(4), push(5), pop(5), pop(4), pop(2)

# Пример 2:

# pushed: 1 2 3

# popped: 3 1 2

# result: False

# Последовательность операций: push(1), push(2), push(3), pop(3), нужно pop(1), но на вершине стека лежит 2.

# Sample Input 1:

# 1 2 3 4 5
# 1 3 5 4 2
# Sample Output 1:

# True
# Sample Input 2:

# 1 2 3
# 3 1 2
# Sample Output 2:

# False

import sys
sys.setrecursionlimit(10000000)

def validate_pushed_popped(pushed: list, popped: list) -> bool:
    n = len(pushed)          # constant
    stack = [0] * (n + 1)    # allocate memory only once
    def _validate(i: int, j: int, p: int) -> bool:
        print(f'i={i}, j={j}, p={p}, stack={stack}')
        if i < 0 or j < 0 or p < 0 or i > n or j > n or p > n:
            return False     # out of boundaries
        if i == n and j == n and p == 0:
            return True      # success
        if p > 0 and stack[p-1] == popped[j] and _validate(i, j+1, p-1):
            return True      # pop successful
        if i == n:           # if we are here with i == n then there's no hope left
            return False
        stack[p] = pushed[i] # try to push
        return _validate(i+1, j, p+1)
    return _validate(0, 0, 0)

def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


solution()

# [+] Test #1. OK
# [+] Test #2. OK
# [+] Test #3. OK
# [+] Test #4. OK
# [+] Test #5. OK
# [+] Test #6. OK
# [+] Test #7. OK
# [+] Test #8. OK
# [+] Test #9. OK
# [+] Test #10. OK
# [+] Test #11. OK
# [+] Test #12. OK
# [+] Test #13. OK
# [+] Test #14. OK
# [+] Test #15. OK
# [+] Test #16. OK
# [+] Test #17. OK
# [+] Test #18. OK
# [+] Test #19. OK
# [+] Test #20. OK
# [+] Test #21. OK
# [+] Test #22. OK
# [+] Test #23. OK
# [+] Test #24. OK
# [+] Test #25. OK
# [+] Test #26. OK
# [+] Test #27. OK
# [+] Test #28. OK
# [ ] Test #29. Runtime error
# [+] Test #30. OK
# [ ] Test #31. Runtime error
# [ ] Test #32. Runtime error
# [ ] Test #33. Runtime error
# [ ] Test #34. Runtime error
# [ ] Test #35. Runtime error
# [ ] Test #36. Runtime error

# 29 of 36 test(s) passed.
