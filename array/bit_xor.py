class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        prev = pref[0]
        res = pref[0]
        result = []
        for idx in range(1, len(pref)):
        # for idx, i in enumerate(pref):
            result.append(res)
            res = prev^pref[idx]
            prev = prev^res
        result.append(res)
        return result


if __name__ == "__main__":
    nums = [5,2,0,3,1] # [5,7,2,3,2]
    s = Solution()
    result = s.findArray(nums)
    pass
