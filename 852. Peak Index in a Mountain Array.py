class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i


###   OR

      
left, right =0, len(arr) - 1
while left < right:
  mid = (left+right)//2
  if arr[mid] < arr[mid+1]:
    left = mid + 1
    else:
      right = mid
return left
                
            
            
        
