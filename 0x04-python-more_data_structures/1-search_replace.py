#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list[:]
    for i in range(len(nlist)):
        if nlist[i] == search:
            nlist[i] = replace
    return(nlist)
