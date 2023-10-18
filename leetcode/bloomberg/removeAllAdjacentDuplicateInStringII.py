class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []

        for c in s:
            if res and res[-1][0] == c:
                res[-1][1] +=1
            else:
                res.append([c, 1])
                

            if res[-1][1]  == k:
                res.pop()

        output = ""

        for char, count in res:
             output += (char * count)

        return output


        