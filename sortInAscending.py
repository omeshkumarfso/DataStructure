arr = [1, 2, 1, 4, 5, 6, 8, 8]
length = len(arr)
temp = arr.copy()
if length % 2 == 0:
    odd = int((length/2)-1)
    even = int(length/2)
else:
    odd = int((length/2))
    even = int(length-odd)

arr.sort()
print("odd=",odd)
print("even=",even)
print(arr)
i= int(0)
j= int(odd)
while True:
    temp[i] = arr[j]
    print("i   j",i,'   ',j)
    if j==0:
        i= int(1)
        j= int(even)
        break 
    i = i+2
    j = j-1
    
while True:
    temp[i] = arr[j]
    if length-1==j:
        break
    i = i+2
    j = j+1

print(temp)
    

