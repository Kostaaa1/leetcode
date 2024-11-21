from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            map[tuple(count)].append(s)

        return map.values()

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    print(sol.groupAnagrams(["x"]))
    print(sol.groupAnagrams([""])) 