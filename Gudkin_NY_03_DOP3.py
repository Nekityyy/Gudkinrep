def count_sets_elements(l):
    result = {}

    all_elements = set().union(*l)

    for element in all_elements:
        count = 0

        for s in l:
            if element in s:
                count += 1

        result[element] = count

    return result

input_list = [input("Введите список")]
print(count_sets_elements(input_list))

