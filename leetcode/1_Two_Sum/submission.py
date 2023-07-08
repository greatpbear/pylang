def twoSum(nums, target):
        mydict = {}
        for x in range(0, len(nums)):
            mydict[nums[x]] = x # get (val, index)
        for x in range(0, len(nums)):
            remain = target - nums[x]
            if remain in mydict:
                if mydict[remain] == x:
                    continue
                return [x, mydict[remain]]

print(twoSum([2,5,9,10],12)) # Expected out: 2+10, so [0,3] 