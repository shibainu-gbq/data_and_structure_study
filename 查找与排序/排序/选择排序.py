import random


def select_sort_simple(li):
    if len(li) == 0:
        return li
    new_li = []
    for i in range(len(li)):
        min_nu = min(li)
        new_li.append(min_nu)
        li.remove(min_nu)
    return new_li


def select_sort(li):
    if len(li) == 0:
        return li

    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

    return li


if __name__ == "__main__":
    test_li = [random.randint(0, 200) for i in range(10)]
    print(test_li)
    print(select_sort_simple(test_li))
    print(select_sort(test_li))
