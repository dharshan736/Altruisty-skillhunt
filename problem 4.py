from collections import Counter

def min_adjacent_swaps(n, A, B):

    if Counter(A) != Counter(B):
        return -1
    
    index_map = {char: [] for char in B}
    for i, char in enumerate(B):
        index_map[char].append(i)
    

    target_positions = []
    for char in A:
        target_positions.append(index_map[char].pop(0))


    def count_inversions(arr):
        """ Use Fenwick Tree (BIT) to count inversions in O(N log N) """
        max_val = max(arr) + 1
        BIT = [0] * (max_val + 1)

        def update(x, delta):
            while x <= max_val:
                BIT[x] += delta
                x += x & -x

        def query(x):
            sum_val = 0
            while x > 0:
                sum_val += BIT[x]
                x -= x & -x
            return sum_val
        
        inv_count = 0
        for i in reversed(arr):
            inv_count += query(i)
            update(i + 1, 1)
        
        return inv_count

    return count_inversions(target_positions)


n = int(input().strip())
A = input().strip()
B = input().strip()

print(min_adjacent_swaps(n, A, B))
