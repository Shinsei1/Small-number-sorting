
def autosort(tab):
    sorting = []
    arr = tuple(tab)
    while sum(tab) != 0:
        for i in range(len(tab)):
            if tab[i] > 0:
                tab[i] -= 1
                if tab[i] == 0:
                    sorting.append(arr[i])
    return sorting



print(autosort([1,4,5,7,8,3,4,7,8]))