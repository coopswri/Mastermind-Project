#the algorithm for a merge sort which takes in an array and orders it
def MergeSort(array):
  if 1 < len(array):
    midpoint = len(array)//2

    left = array[:midpoint]
    right = array[midpoint:]

    MergeSort(left)
    MergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        array[k] = left[i]
        i += 1
        k += 1
      else:
        array[k] = right[j]
        j += 1
        k += 1

    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1

  return array
        
    
