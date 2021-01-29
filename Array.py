arr = []
while True:
    inp = input()
    if inp == "":
        break
    arr.append(int(inp))
print('arr=',arr)
arrCopy = arr.copy()
print('arrCopy=',arrCopy)
findElement = int(input('element to rotate'))
print('findElement=', findElement)
temp = []
print('length of array',len(arr))
for i in range(len(arrCopy)):
    print("i=",i)
    if findElement == arrCopy[i]:
        temp.append(int(arrCopy[i]))
        arr.pop(i)
        break
    else:
        temp.append(int(arrCopy[i]))
        arr[i] = 'null'

# Remove null from list
j = 0
while j< len(arr):
    if arr[j] == 'null':
        arr.pop(j)
        j = 0
    else:
        j = j+1
arr.extend(temp)
print(arr)