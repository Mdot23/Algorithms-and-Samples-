# Determine if the old_list has changed since the new_list 
def get_new_elem(old_list, new_list):
    new_elems = []
    for elem in new_list:
        if elem not in old_list:
            new_elems.append(elem)
    return new_elems

