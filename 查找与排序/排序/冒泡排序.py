import random


def bubble_sort(li):
    if len(li) == 0:
        return li
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


def bubble_sort_01(li):
    if len(li) == 0:
        return li
    for i in range(len(li) - 1):
        exchange_tag = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange_tag = True
        if not exchange_tag:
            return li

    return li


if __name__ == '__main__':
    random_li = [random.randint(0, 10000) for i in range(100)]
    print(random_li)
    print(bubble_sort(random_li))
