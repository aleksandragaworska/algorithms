
def insertion_sort_recursive(not_sorted):
    list_to_sort = not_sorted.copy()

    if len(list_to_sort) == 0:
        return list_to_sort

    def swap(list_to_sort, idx):
        prev_idx = idx - 1
        current_elem = list_to_sort[idx]
        list_to_sort[idx] = list_to_sort[prev_idx]
        list_to_sort[prev_idx] = current_elem

    def recursive_insertion(list_to_sort, idx):
        if idx == 0:
            return
        if list_to_sort[idx] >= list_to_sort[idx - 1]:
            return
        swap(list_to_sort, idx)
        idx -= 1
        recursive_insertion(list_to_sort, idx)

    current_elem = list_to_sort[0]

    for j, elem in enumerate(list_to_sort[1:], 1):
        if elem < current_elem:
            recursive_insertion(list_to_sort, j)
        else:
            current_elem = elem

    return list_to_sort


def insertion_sort_for(not_sorted):
    pass
