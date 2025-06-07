# Problem: Kevin scores points for substrings starting with vowels,
#   Stuart for substrings starting with consonants. Count and print winner.
# Input: one uppercase string S
# Output: “Kevin <score>”, “Stuart <score>” or “Draw”

def minion_game(s):
    vowels = "AEIOU"
    kevin = stuart = 0
    length = len(s)
    for i, ch in enumerate(s):
        points = length - i
        if ch in vowels:
            kevin += points
        else:
            stuart += points
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == "__main__":
    s = input().strip()
    minion_game(s)
