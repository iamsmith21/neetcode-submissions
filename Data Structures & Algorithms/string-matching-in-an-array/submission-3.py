class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort()
        myArr = []

        # ['as', 'hero', 'mass', 'superhero']

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    myArr.append(words[i])
                    break

        return myArr


            

