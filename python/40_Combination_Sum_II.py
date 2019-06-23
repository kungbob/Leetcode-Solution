class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        combination = []
        temp = []
        self.dfs(combination, temp, target, candidates, 0)
        return combination
    
    def dfs(self, combination, temp, target, candidates, index):
        if target < 0:
            return
        
        if target == 0:
            combination.append(temp[:])
            
        for i in range(index, len(candidates)):
            if target < candidates[i]:
                break
                
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            
            temp.append(candidates[i])
            self.dfs(combination, temp, target - candidates[i], candidates, i + 1)
            temp.pop()