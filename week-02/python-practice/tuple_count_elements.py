def count_elements(data: tuple) -> dict:
    summary = {}
    for element in data:
        summary[element] = summary.get(element, 0) + 1

    return summary


tuple_input = (1, 2, 2, 3, 3)
result = count_elements(tuple_input)
print(result)