def find(search_list, value):
    def recursive(left, right):
        if left > right:
            raise ValueError("value not in array")
        mid = (left + right) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            return recursive(mid + 1, right)
        else:
            return recursive(left, mid - 1)
    return recursive(0, len(search_list) - 1) 



