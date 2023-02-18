class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted_words = [word for word in s.split(' ') if word!='']
        return len(splitted_words[len(splitted_words)-1])