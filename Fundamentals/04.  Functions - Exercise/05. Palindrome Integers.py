def palindrome_or_not(nums):

    for el in nums:
        if el == el[:: -1]:
            print(True)
        else:
            print(False)


given_list = input().split(", ")
palindrome_or_not(given_list)
