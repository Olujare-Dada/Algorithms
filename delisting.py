elem_list = []
def delist(list_obj):
    
    for elem in list_obj:
        if isinstance(elem, list):
            print(elem)
            delist(elem)

        else:
            print(elem)
            elem_list.append(elem)
    return elem_list




