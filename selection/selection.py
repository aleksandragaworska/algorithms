
def selection_sort_recursive(not_sorted):

    not_sorted = not_sorted.copy()

    def recursive_select(not_sorted, sorted_list):
        if len(not_sorted) == 0:
            return sorted_list
        min_val = min(not_sorted)
        sorted_list.append(min_val)
        not_sorted.remove(min_val)
        return recursive_select(not_sorted, sorted_list)

    return recursive_select(not_sorted, [])


def selection_sort_for(not_sorted):
    not_sorted = not_sorted.copy()
    sorted_list = []
    for i in range(len(not_sorted)):
        min_val = min(not_sorted)
        sorted_list.append(min_val)
        not_sorted.remove(min_val)
    return sorted_list


def selection_sort_swap(not_sorted):
    not_sorted = not_sorted.copy()

    def swap(my_list, next_index, value):
        to_swap_index = my_list.index(value, next_index)
        old_value = my_list[next_index]
        my_list[next_index] = value
        my_list[to_swap_index] = old_value
        return my_list

    for i in range(len(not_sorted)):
        min_val = not_sorted[i]
        for elem in not_sorted[i:]:
            min_val = min(min_val, elem)
        not_sorted = swap(not_sorted, i, min_val)

    return not_sorted


def selection_sort_swap_2(not_sorted):
    not_sorted = not_sorted.copy()

    def swap(my_list, next_index, to_swap_index):
        old_value = my_list[next_index]
        my_list[next_index] = my_list[to_swap_index]
        my_list[to_swap_index] = old_value
        return my_list

    for i in range(len(not_sorted)):
        min_val = not_sorted[i]
        min_idx = i
        for j, elem in enumerate(not_sorted[i:], i):
            if elem < min_val:
                min_val = elem
                min_idx = j
        not_sorted = swap(not_sorted, i, min_idx)

    return not_sorted


def selection_sort_swap_3(not_sorted):
    not_sorted = not_sorted.copy()

    def swap(my_list, next_index, to_swap_index):
        old_value = my_list[next_index]
        my_list[next_index] = my_list[to_swap_index]
        my_list[to_swap_index] = old_value
        return my_list

    for i in range(len(not_sorted)):
        min_val = not_sorted[i]
        min_idx = i
        for j in range(i, len(not_sorted)):
            elem = not_sorted[j]
            if elem < min_val:
                min_val = elem
                min_idx = j
        not_sorted = swap(not_sorted, i, min_idx)

    return not_sorted
