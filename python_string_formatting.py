# Problem: Read integer n. Print numbers 1→n, their squares and cubes,
#   right-aligned in columns of width 5.
# Input: n
# Output: table of 1 to n

if __name__ == "__main__":
    n = int(input())
    for i in range(1, n+1):
        print(f"{i:>5}{i*i:>5}{i*i*i:>5}")
