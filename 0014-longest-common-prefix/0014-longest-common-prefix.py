class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        first_prefix = [ first[0:i+1] for i in range(0, len(first))]
        strs.remove(first)
        for string in strs:
            for i, prefix in enumerate(first_prefix):
                if prefix != string[0:len(prefix)]:
                    first_prefix = first_prefix[0:i]
                    break
        if len(first_prefix) == 0:
            return ""
        else:
            return first_prefix[len(first_prefix)-1]