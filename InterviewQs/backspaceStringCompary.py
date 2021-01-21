class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.editString(S) == self.editString(T)

    def editString(self, string):
        letters = [];
        for letter in string:
            if letter == "#":
                if len(letters) > 0:
                    lbacetters.pop()
            else:
                letters.append(letter)
        return letters


