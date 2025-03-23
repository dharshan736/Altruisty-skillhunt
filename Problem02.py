def preprocess_treasure_count(s):
    prefix = [0] * (len(s) + 1)
    
    for i in range(1, len(s) + 1):
        prefix[i] = prefix[i - 1] + (1 if s[i - 1] == 'T' else 0)
    
    return prefix

def count_treasures(prefix, start, end):
    return prefix[end] - prefix[start - 1]

s = input().strip()
n = int(input())
prefix = preprocess_treasure_count(s)

for _ in range(n):
    start, end = map(int, input().split())
    print(count_treasures(prefix, start, end))
