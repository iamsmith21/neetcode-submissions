class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # ['as', 'hero', 'mass', 'superhero']

        fullText = " ".join(words)
        return [w for w in words if fullText.count(w) > 1]

       


            

