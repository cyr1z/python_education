def binary_search(s_list, item):
    first = 0
    last = len(s_list) - 1
    result = None

    while first <= last and not result:
        start_position = (first + last) // 2
        if s_list[start_position] == item:
            result = start_position
        else:
            if item < s_list[start_position]:
                last = start_position - 1
            else:
                first = start_position + 1

    return result


if __name__ == "__main__":
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 13))
