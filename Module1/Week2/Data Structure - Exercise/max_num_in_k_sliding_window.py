def max_num_sliding_window(num_list, k):
    if len(num_list) < k or k < 1:
        return []

    lst_max_nums = []
    for i in range(len(num_list) - k + 1):
        sld_window = num_list[i:i + k]
        lst_max_nums.append(max(sld_window))

    return lst_max_nums


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = int(input(''))

    result = max_num_sliding_window(num_list, k)
    print(result)
