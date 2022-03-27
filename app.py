from typing import List, Union

numeric = Union[int, float]


def find_target(arr: List[numeric], target: numeric) -> numeric:
    """Find rightmost value less than or equal to target"""
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if target < arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    return arr[lo - 1]


def rightmost_value_in_sorted_array(arr: List[numeric], target: numeric) -> numeric:
    """
    Find the rightmost value less than or equal to target in arr sorted array.
    :param arr: sorted array [int, float]
    :param target: target value [int, float]
    :return: the rightmost value or -1 if not found/error
    """
    # Edge cases
    if type(target) in [int, float]:
        if len(arr) == 0:
            return -1
        elif len(arr) == 1:
            return arr[0]
        elif target <= arr[0]:
            return arr[0]
        elif target >= arr[-1]:
            return arr[-1]
        # Binary search
        else:
            return find_target(arr, target)

    return -1


if __name__ == "__main__":
    a = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]
    t = [12, 13]
    for i in t:
        print(f"Output: {rightmost_value_in_sorted_array(a, i)}")
