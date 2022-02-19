class Solution:
    def isValid(self, word):
        # vowels = {"a","e","i","o","u"}
        return len(self.vowels-set(word)) == 0 and self.allVowels(word)

    def allVowels(self, word):
        return len(set(word) - self.vowels) == 0

    def countVowelSubstrings(self, word: str) -> int:
        if(len(word) < 5):
            return 0

        self.vowels = {"a", "e", "i", "o", "u"}
        j = 5
        count = 0
        for i in range(len(word)-4):
            j = i+3
            if(word[i] not in self.vowels):
                continue
            while True:
                if(i+j > len(word)):
                    break
                if(word[i+j-1] not in self.vowels):
                    break
                if(self.isValid(word[i:i+j])):
                    print(word[i:i+j])
                    count += 1
                    j += 1
                    continue
                if(self.allVowels(word[i:i+j])):
                    j += 1
                    continue
                else:
                    break

        return count


print(Solution().countVowelSubstrings("cuaieuouac"))
