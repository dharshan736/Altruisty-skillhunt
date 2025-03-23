from collections import deque

def min_of_max_brightness(k, brightness):
    dq = deque()
    max_values = []

    for i in range(k):
        while dq and brightness[dq[-1]] <= brightness[i]:
            dq.pop()
        dq.append(i)

    for i in range(k, len(brightness)):
        max_values.append(brightness[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and brightness[dq[-1]] <= brightness[i]:
            dq.pop()

        dq.append(i)

    max_values.append(brightness[dq[0]])

    return min(max_values)


k = int(input())
n = int(input())
brightness = list(map(int, input().split()))

print(min_of_max_brightness(k, brightness))
