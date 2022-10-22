# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(list(s)) == sorted(list(t))
