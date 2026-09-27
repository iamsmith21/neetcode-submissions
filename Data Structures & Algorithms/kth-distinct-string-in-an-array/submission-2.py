class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        myList = {}

        for i in range(len(arr)):
            myList[arr[i]] = myList.get(arr[i], 0) + 1
            
        res = [key for key, value in myList.items() if value <= 1]

        if len(res) < k:
            return ""

        return res[k - 1]