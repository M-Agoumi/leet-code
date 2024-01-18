class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for str in strs:
            res += str + ":#:"
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        strs = str.split(":#:")
        for str in strs:
            if (str):
                res.append(str)
        return res
    
sol = Solution()
strs = ["lint","code","love","you"]
print(sol.encode(strs))
print(sol.decode(sol.encode(strs)))