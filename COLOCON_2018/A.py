a, b = map(int, input().split())
name = input()

print('YNEOS'[not(a<=len(name) and len(name)<=b)::2])
