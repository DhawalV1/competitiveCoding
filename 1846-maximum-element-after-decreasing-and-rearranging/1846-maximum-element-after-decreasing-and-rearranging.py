class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        
        if arr[0]==1:
        
            for i in range(len(arr)-1):

                if arr[i+1]-arr[i]>1:
                    arr[i+1] = arr[i]+1

            return arr[-1]
        
        else:
            
            arr[0] = 1
            
            for i in range(len(arr)-1):

                if arr[i+1]-arr[i]>1:
                    arr[i+1] = arr[i]+1

            return arr[-1]
            