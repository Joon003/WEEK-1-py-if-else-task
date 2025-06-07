# Problem: Compress a string by counting consecutive identical chars.
#   e.g. “aaabbc” → “a3b2c1”
# Input: one string
# Output: compressed form

from itertools import groupby

if __name__ == "__main__":
    s = input().strip()
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    print("".join(result))
