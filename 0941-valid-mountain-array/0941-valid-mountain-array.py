class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
    
        # Step 1: Check if length is less than 3
        if n < 3:
            return False

        # Step 2: Find the peak
        i = 0
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False  # Peak cannot be at either end

        # Step 3: Check if elements after the peak are strictly decreasing
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        # Step 4: Check if all elements have been traversed
        return i == n - 1

        # Example usage:
        