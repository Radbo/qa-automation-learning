def pairs_to_dict(pairs: list[tuple]) -> dict:
    pairs_dict = {}
    for key, value in pairs:
        pairs_dict[key] = value
    
    return pairs_dict


pairs = [("name", "Sergey"), ("job", "QA")]
pairs_dict = pairs_to_dict(pairs)
print(pairs_dict)