class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i in range(len(nums)):
            num = nums[i]
            c = target - num
            if c in map:
                return [map[c], i]

            map[num] = i

        return []

if __name__ == "__main__":
    sol = Solution() 
    print(sol.twoSum([3,4,5,6], 7)) # 0, 1
    print(sol.twoSum([4,5,6], 10)) # 0, 2
    print(sol.twoSum([5,5], 10)) # 0, 1