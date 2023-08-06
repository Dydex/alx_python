def common_elements(a, b):
    set_1 = set (a) 
    set_2 = set (b)
    empty_list = []
    
    if (set_1 & set_2):
        print(sorted(list(set_1 & set_2)))
    else:
        print (empty_list)
    