pos = -1 

def search(list, n):
    l = 0
    u = len(list) -1 

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
          globals()['pos'] = mid
          return True 

        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid + 1 
        return False



list = [4, 7, 12, 20, 30, 40, 50, 66, 72, 82, 85]
n = 4

if search(list, n):
    print("Found at", pos+1)
else:
    print("Not found")