import heapq


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    return list(heapq.merge(*lists))


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)


print("Відсортований список:", merged_list)
# Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
