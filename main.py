#Python Program to add the corresponding elements of two arrays
#@Author : Sudip Mitra
N = int(input("Enter the number of Array Element :"))

# Get the array 
numArray1 = list(map(int, input("Enter 1st Array Elements :").split()))
numArray2 = list(map(int, input("Enter 2nd Array Elements").split()))

sumArray = []

# logic :
for i in range(0,N):
    sumArray.append(numArray1[i] + numArray2[i])



# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")
