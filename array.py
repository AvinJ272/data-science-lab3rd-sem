import numpy as np

arr=np.array(42)
print(arr)

arr=np.array([1,2,3,4])
print(arr)

arr=np.array([[1,2,3,45],[1,2,3,4]])
print(arr)

arr=np.array([[[1,2,3,],[1,2,5]],[[1,2,5],[1,2,5]]])
print(arr)


arr=np.array([1,2,3,4])
print(arr[0])
print(arr[2])
print(arr[3])


arr=np.array([[8,9,6,7,10],[1,2,3,4,5]])
print('2nd element on 1st row:',arr[0,1])



arr=np.array([[8,9,6,7,10],[1,2,3,4,5]])
print('2nd element on 2st row:',arr[1,4])

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])


arr = np.array([1,2,3,4,5,6,7])
print(arr[4:])

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:1,0:2])


arr = np.array([[1,2,3,4],[5,6,7,8]])


print(arr[0:4,:2])

print(arr[0,:2])

print(arr[0:,:3])

print(arr[0:,:2])

print(arr[0:,1:3])

print(arr[0:,2:4])

print(arr[1:,2:])


