pos = -1 

def search(sequence, n):
    l = 0
    u = len(sequence)-1 

    while l <= u:
        mid = (l+u) // 2

        if sequence[mid] == n:
          globals()['pos'] = mid
          return True 
        else:
            if sequence[mid] < n:
                l = mid + 1
            else:
                u = mid - 1 
    return False



sequence = [4, 7, 12, 20, 30, 40, 50, 66, 72, 82, 85]
n = 7

if search(sequence, n):
    print("Found at", pos+1)
else:
    print("Not found")