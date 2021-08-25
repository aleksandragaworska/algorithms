
def bubble_sort(not_sorted):
    list_to_sorted = not_sorted.copy()

    def swap(swapped_list, current_idx):
        previous_idx = current_idx - 1
        current_elem = swapped_list[current_idx]
        swapped_list[current_idx] = swapped_list[previous_idx]
        swapped_list[previous_idx] = current_elem

    for _ in range(len(list_to_sorted)):
        max_elem = list_to_sorted[0]
        for idx, elem in enumerate(list_to_sorted[1:], 1):
            if elem < max_elem:
                swap(list_to_sorted, idx)
            else:
                max_elem = elem

    return list_to_sorted
