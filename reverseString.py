# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

#  Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


def reverseString(self, s)->None:
    
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right -1)
   
    helper(0, len(s)-1)  
     
    #print(s)     


    


print(reverseString(0,["h","e","l","l","o"]))