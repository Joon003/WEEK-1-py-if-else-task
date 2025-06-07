# Problem: Read n, then n words. Count occurrences, preserve insertion order.
# Input:
#   n
#   w1 w2 ... wn
# Output:
#   number of distinct words
#   counts in order of first appearance

if __name__ == "__main__":
    from collections import OrderedDict
    n = int(input())
    counts = OrderedDict()
    for word in input().split():
        counts[word] = counts.get(word, 0) + 1
    print(len(counts))
    print(*counts.values())
