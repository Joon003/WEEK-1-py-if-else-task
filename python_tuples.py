# Problem: Read n and n space-separated ints. Create a tuple.
#   Print the hash of that tuple.
# Input:
#   n
#   a1 a2 ... an
# Output: hash(tuple)

if __name__ == "__main__":
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))
