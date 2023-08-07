def best_score(a_dictionary):
    if not  a_dictionary:
        return None
    
    best_key = None
    value = best_score
    best_score = int

    for key, value in a_dictionary:
        if value > best_score:
            best_score = value
            best_key = key
    return best_key

    
