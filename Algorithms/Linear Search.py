gnames = ["Amelia", "Olivia", "Isla", "Emily", "Poppy", "Ava", "Isabella", "Jessica", "Lily", "Sophie"]


def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(search(gnames, "Lily"))


def linear_search(list,item):
    i = 0
    while i < len(list):
        if list[i] == item:
            return i
        #end if
        i = i + 1
    #end while
    return -1
#end function

print(linear_search(gnames,"Lily"))
