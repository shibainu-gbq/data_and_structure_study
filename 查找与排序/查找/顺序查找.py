def linear_search(li_set, val):
    """
    :param li_set: 要查找的列表
    :param val: 要查找的数值
    :return: 对应数值的下标
    """
    for index, value in enumerate(li_set):
        if value == val:
            return index
    else:
        return None
