def longest_nonincreasing_subsequence(arr):
    n = len(arr)
    lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] >= arr[i]:
                lengths[i] = max(lengths[i], lengths[j] + 1)

    max_length = max(lengths)

    sequence = []
    current_length = max_length
    for i in range(n - 1, -1, -1):
        if lengths[i] == current_length:
            sequence.append(arr[i])
            current_length -= 1
    sequence.reverse()

    return sequence

# Пример
arr = [5, 3, 8, 4, 2, 7, 6, 1]
result = longest_nonincreasing_subsequence(arr)
print("Наибольшая невозрастающая последовательность:", result)
