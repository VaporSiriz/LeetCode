class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        index = re.search(needle, haystack)
        return index.start() if index else -1