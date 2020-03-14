# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
  
        count = 1;
        fast = 1;
        slow = 0;
        
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                count += 1;
                slow = fast;
                fast = slow +1;
            else:
                del nums[fast];
        print(nums)         
          
        return count


#solution
# i check if the current value is equal to the next value. If true, I delete the next number. Else increase the value of count 
# and increase the counts of the current value index and the next value index.         