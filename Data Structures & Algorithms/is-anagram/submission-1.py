class Solution:
    def makeMap(self, s: str) -> dict:
        dictionary = {}

        for i in s:
            if i in dictionary:
                dictionary[i] += 1;
            else:
                dictionary[i] = 1;

        return dictionary

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = self.makeMap(s)
        tDict = self.makeMap(t)
        
        for char, sCount in sDict.items():
            tCount = tDict.get(char, 0)

            if sCount != tCount:
                return False

        return True;