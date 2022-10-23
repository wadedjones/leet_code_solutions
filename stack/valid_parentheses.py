# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.


def is_valid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            else:
                if not matches(stack.pop(), ch):
                    return False
    return len(stack) == 0

def matches(l: str, r: str) -> bool:
    left = '({['
    right = ')}]'
    return left.index(l) == right.index(r)
