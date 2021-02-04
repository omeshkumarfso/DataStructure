arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
newArr = []
# while True:
#     num = input()
#     if num == '':
#         break
#     arr.append(num)

for i in range(len(arr)):
    if i in arr:
        newArr.append(i)
    else:
        newArr.append(-1)
print(newArr)