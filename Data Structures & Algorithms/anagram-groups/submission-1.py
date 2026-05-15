class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        list2=[]
        for x in range(len(strs)):
            ans[''.join(sorted(strs[x].lower()))].append(strs[x])
        ans2 =[]
        for z in ans:
            ans2.append(ans[z])
        return ans2