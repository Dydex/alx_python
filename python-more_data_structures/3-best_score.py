def best_score(a_dictionary):
    if not  a_dictionary:
        return None
    
    key = best_key


    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key = key
    return best_score

    
