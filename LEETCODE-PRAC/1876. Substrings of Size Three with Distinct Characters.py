class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i,j,c = 0,2,0
        while(j<=len(s)-1):
            if len(set(s[i:j+1])) == 3:
                c += 1
            i += 1
            j += 1
        return c