
def merge_array(left, right):

    result = []

    i = 0
    j = 0

    m = len(left)
    n = len(right)

    # Compare elements of left and right
    while i < m and j < n:

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements of left
    if i < m:
        while i < m:
            result.append(left[i])
            i += 1

    # Add remaining elements of right
    if j < n:
        while j < n:
            result.append(right[j])
            j += 1

    return result


def mergesort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Recursively sort both halves
    left = mergesort(left_arr)
    right = mergesort(right_arr)

    # Merge sorted halves
    return merge_array(left, right)


arr = [7, 5, 4, 2, 1, 45, 67, 12, 500, 234]

print(mergesort(arr))