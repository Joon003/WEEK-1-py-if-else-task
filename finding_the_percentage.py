# Problem: Given N students’ names and marks in 3 subjects,
#   then a query name. Print that student’s average to 2 decimal places.
# Input:
#   N
#   name1 m1 m2 m3
#   ...
#   query_name
# Output: formatted average (e.g. 75.33)

if __name__ == "__main__":
    n = int(input())
    data = {}
    for _ in range(n):
        name, *marks = input().split()
        data[name] = list(map(float, marks))
    query = input().strip()
    avg = sum(data[query]) / len(data[query])
    print(f"{avg:.2f}")
