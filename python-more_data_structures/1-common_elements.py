def common_elements(set_1, set_2):
    common_elements_set = set_1 & set_2
    
    if (common_elements_set):
        print(list(common_elements_set))
    else:
        print ("no common elemnts")
    return common_elements_set