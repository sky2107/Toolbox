# 

arr = [-1, 3, 8, 2, 9, 5]
arr_2 = [4, 1, 2, 10, 5, 20]

target = 24

# writing a function 3 parameters above 
# returns the sum of pairs as closest to the target

# compare all
def add_cobine(arr_1: list, arr_2, target: int):
    # sort them 
    nearest_pair = None
    distance = None
    listi = []
    sumi = []


    for left in arr_1:
        for right in arr_2:
            new_pair = left + right
            if nearest_pair:
                dist = abs(new_pair - target)
                if distance > dist:
                    distance = dist
                    nearest_pair = new_pair
                    listi = []
                    listi.append((left,right))
                elif distance == dist:
                    listi.append((left,right))
            else:
                nearest_pair = left + right
                distance = abs(nearest_pair - target)
                listi.append((left,right))
                sumi.append(distance)

    print(listi)
    print(distance)

add_cobine(arr, arr_2, target)
# permutation len(arr)! possibilities

a = sorted(arr)
b = sorted(arr_2)

def cleverWay():
    target = 24
    distance = None
    running = True
    arr = [-1, 3, 8, 2, 9, 5]
    arr_2 = [4, 1, 2, 10, 5, 20]
    arr = sorted(arr)
    arr_2 = sorted(arr_2)
    for a in arr:
        c = target - a
        if c in arr_2:
            print('Found')
            break

        i = 0
        distance = abs(c + arr_2[i])
        arr_copy = set(arr_2)

        while running:
            i += 1
            if target < a + arr_copy[i]:
                id
            
            
        # for b in arr_2:


print(max(a))
print(max(b))

cleverWay()

