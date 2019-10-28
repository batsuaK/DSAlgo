a = input("Enter the array of numbers :")
# print(a)
arr = a.split(" ")
for i in range(0,len(arr)):
    arr[i] = int(arr[i])
# print(arr)

k = int(input("Enter the total :"))
# print(k)

arr.sort()
# print(arr)
index1 = 0
index2 = len(arr) - 1

while True :
    temp = arr[index1] + arr[index2]
    # print(temp)
    if index2 == index1:
        print("not found")
        exit()
    elif temp == k:
        break
    elif temp > k:
        index2 -=1
    elif temp < k:
        index1 +=1

b = []
b.append(arr[index1])
b.append(arr[index2])
print(b)


# The logic is to have two indexes at the start and end of the sorted input list 
# and move left or right depending on the summation of the total of the two values at the indexes 
# compared to the input.