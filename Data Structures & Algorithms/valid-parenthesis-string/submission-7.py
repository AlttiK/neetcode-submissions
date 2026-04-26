class Solution:
    def checkValidString(self, s: str) -> bool:
        openingParens = []
        stars = []

        for i, c in enumerate(s):
            if c == '(':
                openingParens.append(i)
            elif c == ')':
                if openingParens:
                    openingParens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
        
        while stars and openingParens:
            starIndex = stars.pop()
            parenIndex = openingParens.pop()
            if parenIndex > starIndex:
                return False
        
        if openingParens:
            return False

        return True

