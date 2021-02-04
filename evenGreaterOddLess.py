arr =[1, 2, 3, 4, 5, 6, 7]
newArr = []
tempNewArr = []
for i in range(len(arr)):
    if i%2==0:
        tempNewArr.append(arr[i])
        pos = arr.index(max(tempNewArr[0:i+1]))
        newArr.append()
    else:
        newArr.append(min(arr[0:i]))
 
print(newArr)