def common_elements(a, b):
    set_1 = set (a) 
    set_2 = set (b)
    
    if (set_1 & set_2):
        print(list(set_1 & set_2))
    else:
        print (None)
    