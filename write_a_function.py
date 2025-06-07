# Problem: Define a function is_leap(year) that returns True if year is leap, else False.
# Input: year (int)
# Output: True or False

def is_leap(year):
    # your logic here
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    yr = int(input())
    print(is_leap(yr))
