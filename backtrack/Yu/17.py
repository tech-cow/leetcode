class Solution(object):
    def letterCombinations(self, string):

        # input : "23"
        # output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        #Edge
        if not string:
            return []

        #Global Variable
        self.dict = {
                    "2":"abc",
                     "3":"def",
                     "4":"ghi",
                     "5":"jkl",
                     "6":"mno", 
                     "7":"pqrs",
                     "8":"tuv",
                     "9":"wxyz"
                    }
        self.res = []


        # Helper function
        def dfs(string, index, temp):
            if len(temp) == len(string):
                self.res.append("".join(x for x in temp))
                return

            for char in self.dict[string[index]]:
                temp.append(char)
                dfs(string, index+1, temp)
                temp.pop()


        # Function Call
        dfs(string, 0, [])
        return self.res
