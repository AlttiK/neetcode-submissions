from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                boxNum = 3 * (i // 3) + j // 3

                if val != ".":
                    if val in rowDict[i] or val in colDict[j] or val in boxDict[boxNum]:
                        return False
                    rowDict[i].add(board[i][j])
                    colDict[j].add(board[i][j])
                    boxDict[boxNum].add(board[i][j])
                

        return True