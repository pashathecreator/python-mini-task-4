def invert_dict(d: dict):
    inverted_dict = dict()
    for key, value in d.items():
        if not isinstance(value, (int, float, str, tuple)):
            raise TypeError()
        
        if (inverted_dict.get(value)) is None:
            inverted_dict[value] = key
            continue   
         
        if isinstance(inverted_dict[value], tuple):
                inverted_dict[value] = inverted_dict[value] + (key,)
        else:
            inverted_dict[value] = (inverted_dict[value], key)
    return inverted_dict

