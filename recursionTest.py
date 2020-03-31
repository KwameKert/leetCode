def reverseString(str):

    helper(0, str)


def helper(index,arr):

    if len(arr) == 0 or index >= len(arr):
        return

    helper(index + 1, arr)
    print(arr[index]) 





reverseString("Kwame")