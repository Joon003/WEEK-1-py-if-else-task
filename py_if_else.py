# Problem: Given three integers a, b, c, determine and print:
#   - "YES" if they can form a non-degenerate triangle
#   - "NO" otherwise
# Input: three space-separated ints
# Output: YES or NO

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    # example condition: check triangle inequality
    if a + b > c and a + c > b and b + c > a:
        print("YES")
    else:
        print("NO")
