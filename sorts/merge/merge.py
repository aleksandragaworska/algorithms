from typing import List


def merge_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    merged_list = []
    a_idx, b_idx = 0, 0

    while len(merged_list) < len(list_a) + len(list_b):
        if a_idx == len(list_a):
            merged_list.append(list_b[b_idx])
            b_idx += 1
        elif b_idx == len(list_b):
            merged_list.append(list_a[a_idx])
            a_idx += 1
        elif list_a[a_idx] < list_b[b_idx]:
            merged_list.append(list_a[a_idx])
            a_idx += 1
        else:
            merged_list.append(list_b[b_idx])
            b_idx += 1

    return merged_list


def merge_sort(not_sorted: List[int]) -> List[int]:
    list_to_sort = not_sorted.copy()

    def recursive_sort(list_to_sort):
        if len(list_to_sort) in (0, 1):
            return list_to_sort
        central_idx = int(len(list_to_sort) / 2)
        list_a, list_b = list_to_sort[:central_idx], list_to_sort[central_idx:]
        return merge_lists(recursive_sort(list_a), recursive_sort(list_b))

    return recursive_sort(list_to_sort)
