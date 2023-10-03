def count_common_elements(lists):
    count_dict = {}

    for lst in lists:
        for element in lst:
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1

    common_count = 0
    for count in count_dict.values():
        if count == len(lists):
            common_count += 1

    return common_count

