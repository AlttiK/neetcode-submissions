from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != ".":
                    if val not in rowDict[i]:
                        rowDict[i].add(board[i][j])
                    else:
                        return False
                    if val not in colDict[j]:
                        colDict[j].add(board[i][j])
                    else:
                        return False
                    boxNum = 3 * (i // 3) + j // 3
                    if val not in boxDict[boxNum]:
                        boxDict[boxNum].add(board[i][j])
                    else:
                        return False
                

        return True