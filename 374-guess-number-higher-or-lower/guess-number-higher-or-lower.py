# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n+1
        while True:
            mid = low +(high-low)//2
            val = guess(mid)
            if val==0:
                return mid
            elif val==1:
                low=mid
            elif val==-1:
                high=mid