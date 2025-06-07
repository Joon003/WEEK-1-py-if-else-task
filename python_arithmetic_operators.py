# Problem: Read two ints a, b. Print:
#   a+b, a−b, a*b, integer division (a//b), float division (a/b), a%b, a**b each on its own line.
# Input: two space-separated ints
# Output: seven lines as above

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a / b)
    print(a % b)
    print(a ** b)
