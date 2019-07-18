class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        counter = collections.Counter(arr1)
        dictC = dict(counter)
        print(counter)
        for c in arr2:
            num = dictC[c]
            result += [int(c)] * num
            while c in arr1:
                arr1.remove(c)
        remainL = list(dict.fromkeys(arr1))
        remainL.sort()
        for c in remainL:
            num = dictC[c]
            result += [int(c)] * num
        return result