#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = list(tuple_a)
    list2 = list(tuple_b)
    if len(list1) < 2 or len(list2) < 2:
        if len(list1) < 2:
            if len(list1) == 0:
                list1.append(0)
            if len(list1) == 1:
                list1.append(0)
        if len(list2) < 2:
            list2 = list(list2)
            if len(list2) == 0:
                list2.append(0)
            if len(list2) == 1:
                list2.append(0)
        tuple_c = (list1[0] + list2[0], list1[1] + list2[1])
        return tuple_c
    else:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple_c
