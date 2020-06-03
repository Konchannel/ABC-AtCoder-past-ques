n = int(input())
coins = set()

for i in range(n):
    coins.add("".join(list(map(str, sorted(list(map(int, input().split())))))))

print(len(coins))
