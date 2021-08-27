from typing import List


def existed_binary_search(search_list: List[int], searched_number: int) -> bool:
    search_list = search_list.copy()

    def recursive_search(search_list: List[int], searched_number: int) -> bool:
        central_idx = int(len(search_list) / 2)
        try:
            central_value = search_list[central_idx]
        except IndexError:
            return False
        if searched_number == central_value:
            return True
        if searched_number > central_value:
            return recursive_search(search_list[central_idx + 1:], searched_number)
        if searched_number < central_value:
            return recursive_search(search_list[:central_idx], searched_number)

    return recursive_search(search_list, searched_number)


def idx_binary_search(search_list: List[int], searched_number: int) -> int:

    def recursive_search(part_list: List[int], searched_number: int, greater_or_less: int, real_index: int = -1) -> int:
        part_len = len(part_list)
        if part_len == 0:
            return -1
        central_idx = int(part_len / 2)
        if greater_or_less == 0:
            real_index = central_idx
        elif greater_or_less == 1:
            real_index += central_idx + 1
        else:
            to_subtract = part_len - central_idx
            real_index -= to_subtract
        central_value = part_list[central_idx]
        if searched_number == central_value:
            return real_index
        if searched_number > central_value:
            return recursive_search(part_list[central_idx + 1:], searched_number, 1, real_index)
        if searched_number < central_value:
            return recursive_search(part_list[:central_idx], searched_number, -1, real_index)

    return recursive_search(search_list, searched_number, 0)
