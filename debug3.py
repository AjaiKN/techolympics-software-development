#**
# * BinarySearchBuggy - implements iterative binary search
# * 
# *

def binarySearch(list, key):
	left = 0 
	right = len(list)-1
	
	while left <= right:
		mid = (right + left) // 2
		if list[mid] == key:
			return mid
		elif list[mid] > key:
			right = mid - 1
		else:
			left = mid + 1
	return -1


list = [5, 9, 10, 12, 15, 17, 21, 25, 32, 44, 54, 65]

# display array contents
print("array to be searched:")
print(list)
print()
	
print()
key=int(input("enter a value to search for or -1 to stop: "))

while (key != -1):
	location = binarySearch(list, key)
	if (location == -1):
		print(""+ str(key) + " was not found ")
	else:
		print(""+ str(key) + " found in location " + str(location))

	print()
	key=int(input("enter a value to search for or -1 to stop: "))
