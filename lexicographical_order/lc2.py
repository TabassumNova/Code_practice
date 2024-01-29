class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
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
        def calc_factorial(n):
            fact = 1
            for i in range(1, n+1):
                fact = fact * i
            return fact


        result = []
        total = calc_factorial(len(nums))
        #  step 1 find breaking point
        while (total):
            print(nums)
            if nums not in result:
                result.append(nums.copy())
            ind1 = -1
            ind2 = -1
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
                reverse(ind1+1)
            total -= 1

        return result




if __name__ == "__main__":
    nums = [1,1,2]
    s = Solution()
    result = s.permute(nums)
    pass