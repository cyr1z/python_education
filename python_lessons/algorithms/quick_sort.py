""" quick sort """

from random import randint


def quicksort(s_list):
    """ iterable quick sort """

    n = len(s_list)
    if n < 2:
        return s_list

    parts = [[0, n - 1]]
    while len(parts):
        part = parts.pop()
        start, finish = part
        base_index = randint(start, finish)
        base = s_list[base_index]
        s_list[base_index], s_list[start] = s_list[start], s_list[base_index]

        item_index = start
        first = start + 1
        last = finish

        while first <= last:
            if s_list[first] < base:
                result = -1
            elif s_list[last] > base:
                result = 1
            else:
                result = 0

            if result < 0:
                item_index = first
            else:
                while last > first:
                    if s_list[last] < base:
                        result = -1
                    elif s_list[last] > base:
                        result = 1
                    else:
                        result = 0

                    if result < 0:
                        item_index = first
                        s_list[last], s_list[first] = s_list[first], s_list[last]
                        last -= 1
                        break

                    last -= 1
            first += 1

        s_list[start], s_list[item_index] = s_list[item_index], s_list[start]

        if start < item_index - 1:
            parts.append([start, item_index - 1])

        if item_index + 1 < finish:
            parts.append([item_index + 1, finish])

    return s_list
