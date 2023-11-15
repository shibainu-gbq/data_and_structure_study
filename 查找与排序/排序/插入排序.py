import random


def insert_sort(li):
    if len(li) == 0:
        return
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
    return li


if __name__ == "__main__":
    test_li = [random.randint(0, 1000) for i in range(10)]
    print(test_li)
    print(insert_sort(test_li))

