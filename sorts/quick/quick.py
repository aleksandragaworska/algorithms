from typing import List


def quick_sort(not_sorted: List[int]) -> List[int]:
    list_to_sort = not_sorted.copy()

    def recursive_quick_sort(list_to_sort):
        if len(list_to_sort) < 2:
            return list_to_sort
        central_idx = int(len(list_to_sort) / 2)
        central_value = list_to_sort[central_idx]
        left_list = []
        right_list = []
        for idx, elem in enumerate(list_to_sort):
            if elem < central_value:
                left_list.append(elem)
            elif idx != central_idx:
                right_list.append(elem)
        return recursive_quick_sort(left_list) + [central_value] + recursive_quick_sort(right_list)

    return recursive_quick_sort(list_to_sort)
