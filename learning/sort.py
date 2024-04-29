#binary search
def binSearch(arr, key, start, end):
    if start > end:
        return start
    mid = (start + end) // 2
    if (key > arr(mid)):
        binSearch(arr, key, mid + 1, end)
    else:
        binSearch(arr, key, start, mid - 1)

#insertionSort
#def insertionSort(arr): #this is my stupid code
 #   n = len(arr)
  #  for i in range(1,n):
   #     while i-1 >= 0 and i < i-1:
    #        arr[i] = arr[i-1]
     #       i -= 2
      #      arr[i-1] = arr[i]

    pass

def insertionSort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        loc = binSearch(arr, key, 0, i - 1)
        arr[loc+1: i + 1] = arr[loc: i]
        arr[loc] = key

#def insertionSort(arr): #i copy and pasted this
 #   n = len(arr)
  #  for i in range(1, n):  # Iterate over the array starting from the second element
   #     key = arr[i]  # Store the current element as the key to be inserted in the right position
    #    j = i-1
     #   while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
      #      arr[j+1] = arr[j]  # Shift elements to the right
       #     j -= 1
        #arr[j+1] = key  # Insert the key in the correct position
  

a = [23, 4, 56, 34, 454, 2]
print(a)
insertionSort(a)
print(a)