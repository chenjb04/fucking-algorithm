# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例： 
# 
#  输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化棋盘
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def isValid(row, col):
            # 判断row行：判断[row,0:col-1]是否有'Q'
            for c in range(col):
                if board[row][c] == 'Q':
                    return False
            # 判断col列：判断[0:row-1,col]是否有'Q'
            for r in range(row):
                if board[r][col] == 'Q':
                    return False
            # 左对角线
            mrow, mcol = row, col
            while mrow > 0 and mcol > 0:  # mrow:0->row-1,mcol:0->row-1
                mrow -= 1
                mcol -= 1
                if board[mrow][mcol] == 'Q':
                    return False
            # 判断(右上角)副对角线：判断[0:row-1,col+1:n]
            vrow, vcol = row, col
            while vrow > 0 and vcol < n - 1:  # vrow:0->row-1,vcol:col+1->n
                vrow -= 1
                vcol += 1
                if board[vrow][vcol] == 'Q':
                    return False
            return True

        # 按行递归
        def backtrack(res, row):
            if row == n:
                temp = []
                for line in board:
                    t = ''.join(line)
                    temp.append(t[:])
                res.append(temp[:])
                return
            # 对该行的每一位置进行判断，找到适合放Q的位置，再递归深入到下一行，
            # 到最后一行记录结果，并从下一行回溯到本行时恢复标记回溯到上行，
            for col in range(len(board[row])):
                if not isValid(row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(res, row+1)
                board[row][col] = '.'
        backtrack(res, 0)
        return res

