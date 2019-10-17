def funkcja_l(a_list, b_list):
    c_list = []
    for i in range(len(a_list)):
        if i % 2 == 0:
            c_list.insert(i, a_list[i])
    for j in range(len(b_list)):
        if j % 2 != 0:
            c_list.insert(j, b_list[j])
    return(c_list)


print(funkcja_l(a_list=[5, 6, 7], b_list=[8, 9, 10]))
