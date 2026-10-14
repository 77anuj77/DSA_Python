def sumOfSquares(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=len(nums)
    index=[i for i in range(1,len(nums)) if n%i==0]

    sum=0
    for j in index:
        sum+=nums[j-1]*nums[j-1]

    return sum


print(sumOfSquares([2,7,1,19,18,3]))