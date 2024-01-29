class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def reverse(start):
            i = start
            j = len(nums) - 1
            while (i < j):
                swap(i, j)
                i += 1
                j -= 1

        ind1 = -1
        ind2 = -1
        #  step 1 find breaking point
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] < nums[i + 1]):
                ind1 = i
                break

        #  if there is no breaking  point
        if (ind1 == -1):
            reverse(0)

        else:
            #  step 2 find next greater element and swap with ind2
            for i in range(len(nums) - 1, -1, -1):
                if (nums[i] > nums[ind1]):
                    ind2 = i
                    break
            swap(ind1, ind2)
            #  step 3 reverse the rest right half
            reverse(ind1 + 1)

        return nums


if __name__ == "__main__":
    nums = [1, 0, -1]
    s = Solution()
    result = s.nextPermutation(nums)
    pass

