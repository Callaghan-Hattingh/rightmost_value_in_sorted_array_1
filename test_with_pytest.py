# test_with_pytest.py
from app import rightmost_value_in_sorted_array


def test_int_input():
    arr = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]
    i = [-1, 0, 1, 2, 12, 13, 2500]
    o = [3, 3, 3, 3, 12, 12, 21]
    assert len(i) == len(o)
    assert all([b == rightmost_value_in_sorted_array(arr, a) for a, b in zip(i, o)])


def test_float_input():
    arr = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]
    i = [-1.1, 0.1, 1.1, 2.1, 12.1, 13.1, 2500.1]
    o = [3, 3, 3, 3, 12, 12, 21]
    assert len(i) == len(o)
    assert all([b == rightmost_value_in_sorted_array(arr, a) for a, b in zip(i, o)])


def test_type_input():
    arr = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]
    i = [None, [], {}, (), dict(), "", "1", [1, 2, 3], (1, 2, 3), {1, 2, 3}]
    o = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert len(i) == len(o)
    assert all(
        [b == rightmost_value_in_sorted_array(arr, a) for a, b in zip(i, o)]
    )  # type: ignore
