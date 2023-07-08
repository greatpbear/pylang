containsDuplicate(nums):
    mydict = {}
    for num in nums:
        if num in mydict:
            return True
        else:
            mydict[num] = num
    return False
