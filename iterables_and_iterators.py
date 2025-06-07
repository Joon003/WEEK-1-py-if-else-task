# Problem: Given space-separated elements and an integer k,
#   count how many combinations of size k have all uppercase.
# Input:
#   elements (space-separated)
#   k
# Output: integer count

from itertools import combinations

if __name__ == "__main__":
    elems = input().split()
    k = int(input())
    count = sum(1 for combo in combinations(elems, k)
                if all(item.isupper() for item in combo))
    print(count)
